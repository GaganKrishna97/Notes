from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Hardcoded MySQL database connection URL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/notesdb"  
# Change user/password/host/port/dbname accordingly if needed

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
