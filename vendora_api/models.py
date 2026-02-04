from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import JSON as MySQLJSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(80), nullable=False)

    is_customer = Column(Boolean, default=False)
    is_vendor = Column(Boolean, default=False)
    last_role = Column(String(20), nullable=True)
    name = Column(String(50), nullable=True)

    profile_img = Column(String(500), nullable=True)
    business_imgs = Column(MySQLJSON, nullable=True)

    notes = relationship("Note", back_populates="user")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    date_created = Column(DateTime, server_default=func.current_timestamp())

    user_id = Column(Integer, ForeignKey("users.uid"), nullable=False)
    user = relationship("User", back_populates="notes")


class Vendor(Base):
    __tablename__ = "vendor"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.uid"), nullable=False)
    name = Column(String(150), nullable=False)
    email = Column(String(120))
    business_name = Column(String(100))
    business_address = Column(String(200))
    phone_number = Column(String(20), nullable=False)
    whatsapp_number = Column(String(20))
    open_duration = Column(String(100))
    payment_type = Column(String(50))
    year_of_establishment = Column(Integer)
    rating = Column(String(10))
    rater_no = Column(Integer)


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.uid"), nullable=False)
    full_name = Column(String(100))
    address = Column(String(200))
    phone = Column(String(20))

