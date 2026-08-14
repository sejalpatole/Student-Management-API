# Contains Create, Read, Update, Delete logic

from sqlalchemy.orm import Session
import models
import schemas


def add_student(db: Session, student: schemas.Student):

    existing_student = db.query(models.Student).filter(
        models.Student.id == student.id
    ).first()

    if existing_student:
        return None

    db_student = models.Student(
        id=student.id,
        name=student.name,
        age=student.age,
        course=student.course
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

# Get All Students
def get_all_students(db: Session):
    return db.query(models.Student).all()


# Get Student By ID
def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


# Delete Student
def delete_student(db: Session, student_id: int):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        return None

    db.delete(student)
    db.commit()

    return student


# Update Student
def update_student(db: Session, student_id: int, updated_student: schemas.Student):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        return None

    student.name = updated_student.name
    student.age = updated_student.age
    student.course = updated_student.course

    db.commit()
    db.refresh(student)

    return student