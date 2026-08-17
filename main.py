from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import models
import crud
from database import engine, get_db
from schemas import Student

app = FastAPI(title="Student Management API - Internship")

# Create database tables
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# Add Student
@app.post("/students")
def add_student(student: Student, db: Session = Depends(get_db)):

    new_student = crud.add_student(db, student)

    if new_student is None:
        raise HTTPException(
            status_code=400,
            detail="Student with this ID already exists"
        )

    return {
        "message": "Student added successfully",
        "student": new_student
    }


# Get All Students
@app.get("/students")
def get_all_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)


# Get Student By ID
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = crud.get_student_by_id(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Update Student
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student,
    db: Session = Depends(get_db)
):

    student = crud.update_student(db, student_id, updated_student)
    # This function receives two inputs: student_id and updated_student. 
    # It calls the update_student function from the crud module to 
    # update the student record in the database. If the student is not found, 
    # it raises an HTTPException with a 404 status code and a message indicating that 
    # the student was not found. If the update is successful, it returns a success message 
    # along with the updated student data.

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully",
        "student": student
    }


# Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = crud.delete_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}