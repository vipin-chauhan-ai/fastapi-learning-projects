from fastapi import APIRouter,Depends,HTTPException
from database import SessionLocal
from user_schemas import CreateUser,UserLogin,RefreshTokenRequest
from user_model import User
from sqlalchemy.orm import Session
import auth

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()
def db_get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/registration")
def user_registration(user:CreateUser,db:Session=Depends(db_get)):
    email_exist = db.query(User).filter(User.email == user.email).first()
    if email_exist:
        raise HTTPException(
            status_code =400,
            detail = "Email Already Exist"
        )
    has_pass = auth.hash_password(user.password)    
    new_user = User(
        name =user.name,
        email = user.email,
        password = has_pass,
        age = user.age,
        course = user.course
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "User" :"User Create Successfully",
        "User ID" : new_user.id,
        "Email":new_user.email
    }
#Loging APi    
@router.post("/login")
def user_login(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(db_get)):
    existing_user = db.query(User).filter(User.email == user.username).first()
    if not existing_user:
        raise HTTPException(
            status_code =400,
            detail = "Invalid Email Or Password"
        )
    verify_password =   auth.verify_password(user.password , existing_user.password)  
    #access token
    access_token = auth.create_access_token(data={"sub":existing_user.email,"type": "access","role":existing_user.role})
    refresh_token =auth.create_refresh_token(data={"sub":existing_user.email,"type": "refresh"})
    if not verify_password:
            raise HTTPException(
                status_code =400,
                detail = "Invalid Email Or Password"
            )
  
    return {
        "Message" : "User Login Successfully",
        "id" : existing_user.id,
        "email" :existing_user.email,
        "access_token":access_token,
        "refresh_token" :refresh_token,
        'role' : existing_user.role,
        "token_type" :"bearer"
    }       
  
#GET Profile    
@router.get("/profile")
def profile(curent_user:str= Depends(auth.get_curent_user),):
    return {
        "curent_user" :curent_user
    }
    
# GET refresh Token    
@router.post("/refresh")
def refresh_token(
    request: RefreshTokenRequest
):
    email = auth.verify_token(
        request.refresh_token,
        "refresh"
    )

    new_access_token = auth.create_access_token(
        data={
            "sub": email,
            "type": "access"
        }
    )

    return {
        "message": "New Access Token Generated",
        "access_token": new_access_token,
        "token_type": "bearer"
    }