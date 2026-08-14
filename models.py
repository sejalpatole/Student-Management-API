# this tells SQLAlchemy that create a table called students having these columns
from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    # this tells SQLAlchemy that create a table called students 
    # or it will automatically generate the table name based on the class name
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    course = Column(String, nullable=False)