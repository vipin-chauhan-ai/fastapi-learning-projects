from fastapi import FastAPI,Depends,HTTPException
from database import engine,Base,SessionLocal
import model,schemas
from sqlalchemy.orm import Session
#Import User Router
from user_route import router
app = FastAPI()
Base.metadata.create_all(bind = engine)
#Include User Router
app.include_router(router)


def db_get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Post Student Data

@app.post("/student",response_model=schemas.StudentResponse)
def create_student(student:schemas.CreateStudent,db:Session=Depends(db_get)):
    new_student = model.Student(
        name = student.name,
        age = student.age,
        course = student.course
    )        
    db.add(new_student) 
    db.commit()
    db.refresh(new_student)
    
    return{
        "Message":"Student created",
        "student":{
           
            "name" :new_student.name,
            "age" :new_student.age,
            "course" :new_student.course
    }
    }
    
 # Get Student Data From Database  

@app.get("/student")
def get_student(db:Session=Depends(db_get)):
    students = db.query(model.Student).all()  #select * from table_name 
    # students = db.query(model.Student).filter(model.Student.id==1).all()
    # students = db.query(model.Student.name,model.Student.course).filter(model.Student.id==2).first()
    if students is None:
        raise HTTPException(status_code=404,
                             detail="student not found"
                             )
    return{
        "message" :"Student info",
         "students" :students
    } 
    
# Update Student Data 
@app.put("/student/{id}")
def update_student(id:int,student:schemas.CreateStudent,db:Session=Depends(db_get)):
    students = db.query(model.Student).filter(model.Student.id==id).first()
    if students is None:
            raise HTTPException(status_code=404,
                                 detail="student not found"
            )
    students.name =student.name
    students.course = student.course
    db.commit()
    db.refresh(students)
    return{
        "message":"Student update successfully",
        "student":{
            "name":students.name,
            "course":students.course,
            "age" :students.age
        }
    }    
    
#Delete Student Data        
@app.delete("/student/{id}")
def delete_student(
    id: int,
    db: Session = Depends(db_get)
):

             
    students = db.query(model.Student).filter(
        model.Student.id == id
    ).first()

    db.delete(students)
    db.commit()

    return {
        "Message": "Student Delete Successfully"
    }