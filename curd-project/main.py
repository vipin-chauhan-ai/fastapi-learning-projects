from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

students ={} #dir
class Student(BaseModel):
    name:str
    age:int
    course:str
#post method
@app.post("/student/{id}")
def add_student(id:int,student:Student):
    if id in students:
        raise HTTPException(
            status_code=404,
            detail="Student Allredy exits"
        )
    students[id] =student.model_dump()
    return{
        "Message":"student add successfully",
        "Student":students[id]
    }
#get Method
@app.get("/student/{id}")
def get_student(id:int):
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student Not exits"
        )
    return{'message':'studentdata',
           'student':students[id]
           }     
#put method    
@app.put("/student/{id}")
def update_student(id:int,student:Student):
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student Not exits"
        )      
    students[id] = student.model_dump()  
    return{
        "message" :"Student update successfully",
        "student":students[id]
    }
# Delete method
@app.delete('/student/{id}')
def delete_student(id:int):
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student Not exits"
        )
    deleteed_student = students.pop(id)   
    return{
        "message":"student deleted",
        "student":deleteed_student
    } 
@app.get("/students")
def get_all_student():
    return{
        "message":"All students Data",
        "students":students
    }           