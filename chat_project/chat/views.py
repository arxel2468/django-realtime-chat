from django.shortcuts import render, redirect
from .models import Message
from django.http import JsonResponse
from chat.consumers import ChatConsumer

def chat_room(request):
    messages = Message.objects.all()
    return render(request, "chat.html", {"messages": messages})

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", "Anonymous")
        request.session["username"] = username  # Store in session
        return redirect("chat_room")

    return render(request, "index.html")

def get_online_users(request):
    return JsonResponse({"online_users": list(ChatConsumer.online_users.values())})