from django.urls import path
from chat.consumers import ChatConsumer, OnlineUsersConsumer

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
    path("ws/online_users/", OnlineUsersConsumer.as_asgi()),
]
