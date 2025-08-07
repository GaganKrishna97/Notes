# Note Taking API

A simple Note Taking REST API built with FastAPI and MySQL.  
This API supports creating, reading, updating, and deleting notes stored in a MySQL database, using SQLAlchemy ORM for database access.

---

## Project Structure

/app
main.py # FastAPI application entrypoint
database.py # MySQL connection & SQLAlchemy setup
models.py # SQLAlchemy Note model and Pydantic schemas
crud.py # CRUD database operations
service.py # Business logic and validation layer
api.py # FastAPI route handlers


---

## Installation

1. Install Python 3.8+ (if not installed).

2. Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


---

## MySQL Setup

1. Install MySQL server and MySQL Workbench.

2. Create the database for the app:

CREATE DATABASE notesdb;


3. Update your `database.py` file with your MySQL credentials (username, password, host, port).

---

## Running the API

uvicorn main:app --reload


Server will start at:  

http://127.0.0.1:8000


---

## API Endpoints

- **POST /notes/**  
  Create a new note.  
  Request body:
{
"title": "Note title",
"content": "Note content"
}


- **GET /notes/**  
List all notes.

- **GET /notes/{id}**  
Get a note by ID.

- **PUT /notes/{id}**  
Update a note by ID.  
Request body same as for create.

- **DELETE /notes/{id}**  
Delete a note by ID.

---

## Documentation

Interactive docs and testing available at:  
http://127.0.0.1:8000/docs


---

## Notes

- Currently using MySQL with SQLAlchemy ORM.
- Business validation is done in the service layer.
- Modify connection details safely for production usage.
- Remember to secure your database credentials and use strong passwords.

---

## Support

Feel free to ask if you need help, or want to extend this project with features like authentication, pagination, or deployment!
