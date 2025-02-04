import json
from channels.generic.websocket import AsyncWebsocketConsumer

online_users = set()  # Track online users

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("chatroom", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chatroom", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        await self.channel_layer.group_send(
            "chatroom",
            {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))

class OnlineUsersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope["user"].username if self.scope["user"].is_authenticated else "Guest"
        online_users.add(self.username)

        await self.channel_layer.group_add("online_users", self.channel_name)
        await self.accept()
        await self.send_online_users()

    async def disconnect(self, close_code):
        online_users.discard(self.username)
        await self.channel_layer.group_discard("online_users", self.channel_name)
        await self.send_online_users()

    async def send_online_users(self):
        await self.channel_layer.group_send(
            "online_users",
            {"type": "online_users_list", "users": list(online_users)}
        )

    async def online_users_list(self, event):
        await self.send(text_data=json.dumps({"users": event["users"]}))
