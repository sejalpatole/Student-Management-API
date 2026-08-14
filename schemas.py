# Defines request and response models
# Defines the database table
from pydantic import BaseModel


class Student(BaseModel):                       # => Student will inherit from BaseModel
    id: int
    name: str
    age: int
    course: str