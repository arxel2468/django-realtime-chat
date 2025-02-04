from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat_room, name="chat_room"),
    path("", views.index, name="index"),
    
]
