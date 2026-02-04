from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Vendor
from database import  SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
       yield db 
    finally:
        db.close()
        
        
db_dependency = Annotated[Session, Depends(get_db)]
        
@router.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Vendor).all()