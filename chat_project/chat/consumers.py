import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    online_users = {}  # Store users uniquely

    async def connect(self):
        self.room_name = "global_chat"
        self.room_group_name = f"chat_{self.room_name}"

        # Get username from query params or set default
        self.username = self.scope["session"].get("username", "Anonymous")
        self.user_id = str(self.channel_name)  # Unique WebSocket channel name

        # Add user to online list
        ChatConsumer.online_users[self.user_id] = self.username

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Send updated user list
        await self.send_online_users()

    async def disconnect(self, close_code):
        # Remove user from online list
        ChatConsumer.online_users.pop(self.user_id, None)

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Send updated user list to all
        await self.send_online_users()

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = self.username  # Ensure correct username is used

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({'message': message, 'username': username}))

    async def send_online_users(self):
        """ Send the updated list of online users """
        user_list = list(set(ChatConsumer.online_users.values()))  # Avoid duplicate names
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_users',
                'users': user_list
            }
        )

    async def update_users(self, event):
        """ Send online users list to the client """
        await self.send(text_data=json.dumps({'online_users': event['users']}))

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            print("Received data:", data)  # Debugging line
            
            if "type" in data and data["type"] == "user_joined":
                self.username = data["username"]
                self.scope["session"]["username"] = self.username  # Store username in session
                ChatConsumer.online_users[self.user_id] = self.username
                await self.send_online_users()
                return  # Avoid processing further
            
            if "message" not in data:
                print("Error: 'message' key not found in received data.")
                return  # Ignore malformed messages
            
            message = data["message"]
            username = self.username  # Ensure correct username is used

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "username": username,
                }
            )
        except json.JSONDecodeError:
            print("Error: Invalid JSON received.")