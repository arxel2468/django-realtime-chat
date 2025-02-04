# Django Real-Time Chat Room

## Features
- Real-time chat using Django Channels and WebSockets
- Online members view updates in real-time
- Uses Redis for WebSocket layer
- Daphne server configuration

## Setup Instructions
```bash
git clone https://github.com/arxel2468/django-realtime-chat.git
cd django-realtime-chat
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Usage
Visit http://127.0.0.1:8000/ for the chat room.
Visit http://127.0.0.1:8000/online_users/ to see online members.