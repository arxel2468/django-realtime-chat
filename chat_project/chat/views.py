from django.shortcuts import render
from .models import Message

def chat_room(request):
    messages = Message.objects.all()
    return render(request, "chat.html", {"messages": messages})

def online_users(request):
    return render(request, "online_users.html")
