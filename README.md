Note Taking API with FastAPI and MySQL
A multi-table REST API for note taking built with FastAPI, SQLAlchemy ORM, and MySQL.

Features
User management: create and retrieve users

Notes management: create, read, update, delete notes linked to users

Tags management: attach multiple tags to notes (many-to-many relationship)

Automatic database table creation on app startup

Simple setup — no .env needed; MySQL creds are hardcoded in database.py

API docs available via Swagger UI at /docs

Project Structure
text
/app
  main.py            # FastAPI app entrypoint, table creation on startup
  database.py        # SQLAlchemy DB setup with MySQL connection string
  models/            # SQLAlchemy models: User, Note, Tag with relationships
    __init__.py
    user.py
    note.py
    tag.py
  crud.py            # Basic DB operations for User, Note, Tag
  service.py         # Business logic and validation layer
  api.py             # FastAPI routes for users, notes, tags
requirements.txt     # Python dependencies
README.md            # This file
Prerequisites
Python 3.8+

MySQL database server running locally (or accessible remotely)

Database named notesdb created in MySQL:

sql
CREATE DATABASE notesdb;

Setup
Clone the repository.

(Optional but recommended) Create and activate a virtual environment:

bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt

Verify your MySQL server is running and accessible.

Check your MySQL credentials in database.py. Default connection string:


python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/notesdb"
Change username/password/host/port/database if needed.


Running the API
Run the FastAPI server with:

bash
uvicorn main:app --reload

Server will start at:
http://127.0.0.1:8000

API Endpoints
Use Swagger UI for interactive API docs and testing:
http://127.0.0.1:8000/docs

Users
POST /users/ — Create a new user by providing { "username": "yourname" }

GET /users/{user_id} — Get details of a user

Notes
POST /users/{user_id}/notes/ — Create a note for a user:

Request body example:

json
{
  "title": "Sample Note",
  "content": "Some note content",
  "tags": ["tag1", "tag2"]
}
GET /users/{user_id}/notes/ — List notes for a user

GET /notes/{note_id} — Get a note by ID

PUT /notes/{note_id} — Update a note by ID

DELETE /notes/{note_id} — Delete a note by ID

Tags
GET /tags/ — List all tags

Notes
Tables (users, notes, tags, note_tag) are created automatically on app startup.

User must be created first before notes can be assigned to them.

Tags are created on-the-fly when adding to notes if they don’t already exist.

Troubleshooting
If you get database connection errors, verify your MySQL credentials and server status.

Make sure the database notesdb exists before running the app (the app does not auto-create the database, only the tables).

Drop and recreate tables if you have schema mismatches (see drop commands below):

sql
USE notesdb;
DROP TABLE IF EXISTS note_tag;
DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;


Then restart the API server.



