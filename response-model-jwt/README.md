# FastAPI JWT Authentication with OAuth2

A practical FastAPI authentication project demonstrating User Registration, Login, JWT Access Token generation, OAuth2 Login and Get User Profile API.

This project is part of my **FastAPI Hindi Tutorial Series**.

## ✅ Features Completed

- User Model using SQLAlchemy
- Request validation using Pydantic
- User Registration API
- Duplicate email validation
- Password hashing using Passlib and Bcrypt
- User Login with email and password
- JWT Access Token generation
- JWT token expiry
- OAuth2 Login using `OAuth2PasswordRequestForm`
- Token extraction using `OAuth2PasswordBearer`
- JWT token decoding and validation
- Get current logged-in user
- Get User Profile API
- Swagger UI authentication testing

## 🔐 Authentication Flow

```text
User Registration
        ↓
Password Hashing
        ↓
User Saved in SQLite Database
        ↓
OAuth2 Login with Username and Password
        ↓
JWT Access Token Generated
        ↓
Token Sent Through Authorization Header
        ↓
JWT Token Decoded and Validated
        ↓
Current User Email Retrieved
        ↓
User Profile Returned
```

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
├── .gitignore
└── README.md
```

## 📄 File Description

| File | Purpose |
|---|---|
| `main.py` | Main FastAPI application and router configuration |
| `database.py` | SQLAlchemy database engine, session and Base configuration |
| `model.py` | Student SQLAlchemy model |
| `schemas.py` | Student Pydantic schemas |
| `user_model.py` | User SQLAlchemy database model |
| `user_schemas.py` | User registration, login and response schemas |
| `user_route.py` | Registration, OAuth2 Login and Profile API routes |
| `auth.py` | Password hashing, JWT generation, OAuth2 scheme and token validation |

## 🛠️ Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- JWT
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

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

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

### 6. Run the FastAPI application

```bash
uvicorn main:app --reload
```

## 📌 Swagger UI

Open the following URL after starting the server:

```text
http://127.0.0.1:8000/docs
```

## 🔑 OAuth2 Login Process

1. Register a new user.
2. Open the OAuth2 Login API.
3. Enter the registered email in the `username` field.
4. Enter the user password.
5. Execute the Login API.
6. Copy the generated JWT Access Token.
7. Use the token to access the Get User Profile API.

## 🧩 JWT Access Token

The JWT token contains the user's email in the `sub` claim:

```python
{
    "sub": "user@example.com",
    "type": "access",
    "exp": "token-expiration-time"
}
```

The token is digitally signed using:

```python
SECRET_KEY
ALGORITHM
```

## 👤 Get Current User

The `get_current_user()` dependency:

- Receives the JWT token using `OAuth2PasswordBearer`
- Decodes the token
- Reads the user email from the `sub` claim
- Returns `401 Unauthorized` for an invalid token
- Provides the authenticated user to the Profile API

## 🎥 FastAPI Hindi Tutorial Series

### User Model, Pydantic Schema and APIRouter

https://youtu.be/R1u4cGOJZUY

### User Registration API

https://youtu.be/Avp8W_JpJeA

### Complete FastAPI Hindi Playlist

https://www.youtube.com/watch?v=ZdXddDsXl2o&list=PLQmLgnwT9Bvg

## 📚 JWT Authentication Notes

https://vipin-chauhan-ai.github.io/vipin-ai-notes/jwt-authentication-questions-%20partical

## 💻 Complete Repository

https://github.com/vipin-chauhan-ai/fastapi-learning-projects

## ⏭️ Upcoming

- Test protected APIs in Postman
- Send JSON data with JWT Bearer Token
- Role-Based Access Control
- Admin and User permissions

## 👨‍💻 Author

**Vipin Chauhan**

Python & FastAPI Developer | Building GenAI, RAG and Agentic AI Applications | Hindi Tech Educator

## ⭐ Support

If this project is helpful, please give the repository a star and subscribe to the YouTube channel for more practical FastAPI Hindi tutorials.