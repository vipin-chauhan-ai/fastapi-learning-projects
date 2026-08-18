from fastapi import APIRouter,Depends,HTTPException
from database import SessionLocal
from user_schemas import CreateUser,UserLogin
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
#USer regisration        
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
        course = user.course,
        role="user"
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
def user_login(user:UserLogin=Depends(),db:Session=Depends(db_get)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(
            status_code =400,
            detail = "Invalid Email Or Password"
        )
    #Verify Password with auth    
    verify_password =   auth.verify_password(user.password , existing_user.password)  
    #access token from auth
    access_token = auth.create_access_token(data={"sub":existing_user.email})
    
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
        "token_type" :"bearer", 
        
    
    }       
    