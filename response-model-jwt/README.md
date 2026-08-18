# FastAPI JWT Authentication Project

A practical FastAPI project demonstrating User Registration, Login, Password Hashing, JWT Authentication, Protected Routes, SQLAlchemy and SQLite.

This project is part of my **FastAPI Hindi Tutorial Series**.

## 🚀 Features

- User Model using SQLAlchemy
- User Registration API
- Duplicate Email Validation
- Secure Password Hashing
- User Login API
- JWT Access Token Generation
- OAuth2 Password Bearer Authentication
- Get Current Logged-in User
- Protected API Routes
- Pydantic Request and Response Schemas
- SQLite Database Integration
- Student CRUD APIs
- Swagger UI Testing

## 📁 Project Structure

```text
response-model-jwt/
│
├── auth.py
├── database.py
├── main.py
├── model.py
├── schemas.py
├── user_model.py
├── user_route.py
├── user_schemas.py
└── README.md
```

## 📄 File Details

| File | Purpose |
|---|---|
| `main.py` | Main FastAPI application and routes |
| `database.py` | Database engine, session and Base configuration |
| `model.py` | Student SQLAlchemy database model |
| `schemas.py` | Student Pydantic schemas |
| `user_model.py` | User SQLAlchemy database model |
| `user_schemas.py` | User registration, login and response schemas |
| `user_route.py` | User registration and login API routes |
| `auth.py` | Password hashing, JWT token and current-user authentication |

## 🛠️ Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- JWT Authentication
- OAuth2
- Passlib
- Bcrypt
- Python-JOSE
- Uvicorn

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vipin-chauhan-ai/fastapi-learning-projects.git
```

### 2. Open the project folder

```bash
cd fastapi-learning-projects/response-model-jwt
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Install required packages

```bash
pip install fastapi uvicorn sqlalchemy pydantic "passlib[bcrypt]" "python-jose[cryptography]" python-multipart
```

### 6. Run the FastAPI server

```bash
uvicorn main:app --reload
```

## 📌 API Documentation

After running the server, open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 🔐 Authentication Flow

```text
User Registration
       ↓
Password Hashing
       ↓
User Saved in Database
       ↓
Login with Email and Password
       ↓
JWT Access Token Generated
       ↓
Token Verified
       ↓
Current User Accesses Protected API
```

## 🎥 FastAPI Hindi Video Tutorials

### User Model, Pydantic Schema and APIRouter

https://www.youtube.com/playlist?list=PLQmLgnwT9Bvg 

### User Registration API

https://youtu.be/Avp8W_JpJeA

### Login API with JWT Access Token

Add login video link here.

## 📂 Complete FastAPI Projects

https://github.com/vipin-chauhan-ai/fastapi-learning-projects

## 📝 AI Developer Notes

https://github.com/vipin-chauhan-ai/vipin-ai-notes

## 📺 YouTube Channel

https://www.youtube.com/@vipin-ai-v3u

## 👨‍💻 Author

**Vipin Chauhan**

Python & FastAPI Developer | Building GenAI, RAG and Agentic AI Applications | Hindi Tech Educator

## ⭐ Support

If this project is helpful, please give the repository a ⭐ and subscribe to the YouTube channel for complete FastAPI Hindi tutorials.
