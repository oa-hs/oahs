import enum
from sqlalchemy import Boolean, Column, Enum, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base


class RoleEnum(str, enum.Enum):
    student = "student"
    mentor = "mentor"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(Text, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    oa_id = Column(String(50))
    lodge_id = Column(String(50))
    chapter = Column(String(100))
    region = Column(String(50))
    industry = Column(String(100))
    graduation_year = Column(Integer)
    employer = Column(String(200))
    bio = Column(Text)
    signup_period = Column(String(20))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
