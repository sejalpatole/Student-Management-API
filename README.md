# Student Management API

A simple RESTful Student Management API built using **FastAPI**, **SQLAlchemy**, **SQLite**, and **Pydantic**.

This project demonstrates how to build a backend API with CRUD operations for managing student records.

## 🚀 Features

* Add a new student
* Get all students
* Get a student by ID
* Update student details
* Delete a student
* SQLite database integration
* SQLAlchemy ORM
* Pydantic data validation
* Interactive Swagger API documentation

## 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic

## 📁 Project Structure

```text
Student Management API/
│
├── main.py              # FastAPI application and API routes
├── crud.py              # Create, Read, Update and Delete operations
├── database.py          # Database connection and session configuration
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas
├── requirements.txt     # Required Python packages
├── README.md            # Project documentation
└── .gitignore           # Files ignored by Git
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Student-Management-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the API

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test all API endpoints directly from Swagger UI.

## 🔗 API Endpoints

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| GET    | `/`                      | Welcome message   |
| POST   | `/students`              | Add a new student |
| GET    | `/students`              | Get all students  |
| GET    | `/students/{student_id}` | Get student by ID |
| PUT    | `/students/{student_id}` | Update student    |
| DELETE | `/students/{student_id}` | Delete student    |

## 🗄️ Database

The project uses **SQLite** as the database and **SQLAlchemy** as the ORM.

The database contains a `students` table with:

* `id`
* `name`
* `age`
* `course`

## 🧪 Example Student

```json
{
  "id": 1,
  "name": "Sejal Patole",
  "age": 18,
  "course": "AIML"
}
```

## 🎯 Learning Objectives

This project was created to practice:

* FastAPI application development
* REST API design
* CRUD operations
* Database integration
* SQLAlchemy ORM
* Pydantic validation
* API testing using Swagger UI
* Python backend development

## 📌 Future Improvements

* Add authentication and authorization
* Add pagination and search
* Add better error handling
* Add response schemas
* Add automated tests
* Deploy the API to a cloud platform

## 👩‍💻 Author

**Sejal Patole**

Student | AI & Machine Learning | Python | FastAPI
