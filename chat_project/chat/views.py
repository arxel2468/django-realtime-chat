from django.shortcuts import render, redirect
from .models import Message

def chat_room(request):
    messages = Message.objects.all()
    return render(request, "chat.html", {"messages": messages})

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", "Anonymous")
        request.session["username"] = username  # Store in session
        return redirect("chat_room")

    return render(request, "index.html")