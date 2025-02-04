Real-Time Chat Application (Django + WebSockets)
This is a real-time chat application built using Django and WebSockets. It supports:
✅ Live messaging with WebSockets
✅ User login with unique names
✅ Sidebar for dynamically updating online users
✅ Improved UI/UX with Bootstrap

📂 Project Structure
    ```bash
    /chat_project/
    │── chat/                        # Django app
    │   ├── migrations/              # Database migrations
    │   ├── static/                  # CSS, JavaScript, and other assets
    │   ├── templates/               # HTML templates
    │   ├── consumers.py             # WebSocket logic
    │   ├── routing.py               # WebSocket routes
    │   ├── urls.py                  # Django URLs
    │   ├── views.py                 # Django views
    │── chat_project/                 # Django main project files
    │   ├── settings.py              # Django settings
    │   ├── urls.py                  # Main project URL routing
    │   ├── asgi.py                  # ASGI entry point for WebSockets
    │── db.sqlite3                   # SQLite database
    │── manage.py                    # Django management script
    │── requirements.txt             # Dependencies
    │── README.md                    # Documentation
🚀 Setup & Installation
1️⃣ Clone the Repository
    ```sh
    git clone https://github.com/arxel2468/real-time-chat.git
    cd real-time-chat
2️⃣ Create a Virtual Environment (Optional but Recommended)
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3️⃣ Install Dependencies
    ```sh
    pip install -r requirements.txt
4️⃣ Apply Migrations
    ```sh
    python manage.py migrate
5️⃣ Start the Development Server
    ```sh
    python manage.py runserver
🔗 Open http://127.0.0.1:8000/ in your browser.

🛠 Features & Functionality
1️⃣ User Login (Unique Names)
Users enter a unique name to join.
If a name is taken, a number is appended automatically (e.g., John1, John2).
2️⃣ Real-Time Chat (WebSockets)
Messages are instantly sent & received using Django Channels.
Messages are displayed in a Bootstrap-styled chat box.
3️⃣ Online Users Sidebar
Dynamically updates the list of currently online users.
4️⃣ Logout Functionality
Users can click Logout to exit and remove themselves from the online users list.
📜 API Endpoints
Method	Endpoint	Description
GET	/	Login Page
GET	/chat/	Chat Room Page
GET	/get_online_users/	Returns list of online users
⚡ WebSocket Events
Event Type	Payload Example	Description
user_joined	{ "type": "user_joined", "username": "John" }	Adds user to the online list
message	{ "message": "Hello", "username": "John" }	Sends a chat message
user_left	{ "type": "user_left", "username": "John" }	Removes user from online list
📌 Additional Notes
✅ Compatible with Django 4+
✅ Uses Django Channels for WebSockets
✅ Designed for real-time applications

🛠 Tech Stack
Django (Backend)
Django Channels (WebSockets)
JavaScript (Frontend logic)
Bootstrap (UI Styling)
