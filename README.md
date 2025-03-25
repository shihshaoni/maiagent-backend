# MaiAgent Backend

A Django-based backend system for managing AI-powered conversations.

## Features

- 🗣️ **Conversation Management**  
  Create, view, and track user-AI conversations.

- 🤖 **AI Auto Reply Flow**  
  Automatically replies to user messages with simple AI responses.

- 🔍 **Advanced Search**  
  Filter and sort messages based on content and timestamp.

- 🔗 **RESTful API**  
  Access conversations and messages through DRF-powered API endpoints.

- 🛠️ **Admin Interface**  
  Full Django admin UI to manage conversations and messages.

## API Endpoints

| Endpoint              | Method | Description               |
|-----------------------|--------|---------------------------|
| `/api/conversations/` | POST   | Create a new conversation |
| `/api/messages/`      | POST   | Send a message            |
| `/api/messages/`      | GET    | Get messages by query     |

## Project Structure
maiagent_backend/
├── config/               # Django settings and URL routing
├── conversation/         # Main app for chat models & views
├── templates/            # Frontend templates
└── test_conversation.py  # Example API test script

## How to Run

```bash
# Install dependencies
pip install -r requirements/local.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver

# Testing
python test_conversation.py



