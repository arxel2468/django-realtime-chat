from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat_room, name="chat_room"),
    path("", views.index, name="index"),
    path("get_online_users/", views.get_online_users, name="get_online_users"),
    
]
