from fastapi import APIRouter,Depends,HTTPException
from database import SessionLocal
from user_schemas import CreateUser
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