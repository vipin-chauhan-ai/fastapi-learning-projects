from pydantic import BaseModel,Field,EmailStr

class CreateUser(BaseModel):
    name:str = Field(...,min_length=5,max_length=20)
    email:EmailStr
    password:str = Field(...,min_length=5,max_length=30)
    age:int = Field(...,ge=18,le=60)
    course:str = Field(...,min_length=5,max_length=30)
class UserLogin(BaseModel):
    email:EmailStr
    password:str
     