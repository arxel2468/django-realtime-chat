from django.urls import path
from .views import chat_room, online_users

urlpatterns = [
    path("", chat_room, name="chat_room"),
    path("online_users/", online_users, name="online_users"),
]
