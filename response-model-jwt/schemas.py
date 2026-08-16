from pydantic import BaseModel,Field

class CreateStudent(BaseModel):
    name:str = Field(...,min_length=5,max_length=20)
    age:int = Field(...,gt=18,lt=50)
    course:str = Field(...,min_length=5,max_length=30)

class StudentResponse(BaseModel):
    # id:int
    # name:str    
    # course:str
    Message:str
    student:CreateStudent