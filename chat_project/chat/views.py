from django.shortcuts import render

def chat_room(request):
    return render(request, "chat.html")

def online_users(request):
    return render(request, "online_users.html")
