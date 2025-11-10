from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.session import get_db

def get_database_session(db: Session = Depends(get_db)):
    return db

# Additional dependency functions can be added here as needed.