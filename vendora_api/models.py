from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.dialects.mysql import JSON as MySQLJSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.ext.mutable import MutableList
from database import Base

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

    is_customer = Column(Boolean, default=False)
    is_vendor = Column(Boolean, default=False)

    last_role = Column(String(20))
    name = Column(String(50))

    # Images
    profile_img = Column(String(500))
    business_imgs = Column(
        MutableList.as_mutable(JSON),
        default=list
    )

    # One-to-one relationships
    customer_profile = relationship(
        "Customer",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    vendor_profile = relationship(
        "Vendor",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        
        return f"<User uid={self.uid}, username={self.username}>"
class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.uid"), nullable=False)

    full_name = Column(String(100))
    address = Column(String(200))
    phone = Column(String(20))

    user = relationship("User", back_populates="customer_profile")

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

    rating = Column(Float)
    rater_no = Column(Integer)

    user = relationship("User", back_populates="vendor_profile")
