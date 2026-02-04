from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Vendor, User
from database import  SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
       yield db 
    finally:
        db.close()
        
        
db_dependency = Annotated[Session, Depends(get_db)]
        
@router.get("/vendors")
async def read_all_vendors(db: Annotated[Session, Depends(get_db)]):
    return db.query(Vendor).all()

@router.get("/users")
async def read_all_users(db: Annotated[Session, Depends(get_db)]):
    return db.query(User).all()

@router.get("/vendors_front")
async def vendors_front(db: Annotated[Session, Depends(get_db)]):
    users = (
        db.query(User)
        .options(joinedload(User.vendor_profile))
        .filter(User.is_vendor == True)
        .all()
    )

    result = []

    for user in users:
        vendor = user.vendor_profile
        if not vendor:
            continue

        result.append({
            "user_id":user.uid,
            "vendor_id":vendor.id,
            "profile_img": user.profile_img,
            "business_imgs": user.business_imgs or [],

            "name": vendor.name,
            "email": vendor.email,
            "business_name": vendor.business_name,
            "business_address": vendor.business_address,

            "phone_number": vendor.phone_number,
            "whatsapp_number": vendor.whatsapp_number,

            "open_duration": vendor.open_duration,
            "payment_type": vendor.payment_type,

            "year_of_establishment": vendor.year_of_establishment,
            "rating": vendor.rating,
            "rater_no": vendor.rater_no,
        })

    return result