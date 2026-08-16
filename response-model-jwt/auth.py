from passlib.context import CryptContext

from jose import JWTError,jwt,ExpiredSignatureError
from datetime import datetime,timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "my-sec-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30 

#VAR

ACCESS_REFRESH_TOKEN_EXPIRE = 7 #days

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)
#hash_password user registration
def hash_password(password:str):
    return pwd_context.hash(password)

# Login user authentication
def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

# Create Access TOKEN
def create_access_token(data:dict):
    to_encoded = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encoded.update({"exp":expire})
    
    encoded_jwt = jwt.encode(
        to_encoded,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt
 