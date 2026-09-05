from fastapi import FastAPI,Depends,HTTPException,Query
from database import engine,Base,SessionLocal
import model,schemas
from sqlalchemy.orm import Session
from sqlalchemy import or_,asc,desc
#Import User Router
from user_route import router
#Import File Router
from file_route import router as file_router
import auth
app = FastAPI()
Base.metadata.create_all(bind = engine)
#Include User Router
app.include_router(router)

#Include file Router
app.include_router(file_router)

def db_get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Post Student Data
@app.post("/student",response_model=schemas.StduentPostResponse)
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
def get_student(db:Session=Depends(db_get),page:int= Query(1,ge=1),limit:int= Query(10,ge=1,le=100),serach:str= Query(None),age:int=Query(None),course:str= Query(None),sort:str=Query(None)):
     offset = (page-1)*limit

     query = db.query(model.Student)
   #Search
     if serach:
        query= query.filter(
            or_(
                model.Student.name.ilike(f"%{serach}%"),
                model.Student.course.ilike(f"%{serach}%"),
            )
        )
    #Filter
     if age:
        query = query.filter(model.Student.age==age)
     if course:
        query = query.filter(model.Student.course==course)   
    #SORTING
     if sort=="asc":
        query = query.order_by(asc(model.Student.name))
     elif sort=="desc":
            query = query.order_by(desc(model.Student.name))  
    #GET ALL STUDENT DATA           
     students = query.offset(offset).limit(limit).all()  
     total_records =query.count()    
     if students is None:
        raise HTTPException(status_code=404,
                             detail="student not found"
                             )
     return{
        "message" :"Student info",
        "page":page,
        "limit" : limit,
        "total_records" : total_records,
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
    curent_user:dict = Depends(auth.require_admin),
    db: Session = Depends(db_get)
):

             
    students = db.query(model.Student).filter(
        model.Student.id == id
    ).first()

    if students is None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    db.delete(students)
    db.commit()

    return {
        "Message": "Student Delete Successfully"
    }