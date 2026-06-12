from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.user import RoleEnum


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: RoleEnum
    first_name: str
    last_name: str
    oa_id: Optional[str] = None
    lodge_id: Optional[str] = None
    chapter: Optional[str] = None
    region: Optional[str] = None
    industry: Optional[str] = None
    graduation_year: Optional[int] = None
    employer: Optional[str] = None
    bio: Optional[str] = None
    signup_period: Optional[str] = None


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    oa_id: Optional[str] = None
    lodge_id: Optional[str] = None
    chapter: Optional[str] = None
    region: Optional[str] = None
    industry: Optional[str] = None
    graduation_year: Optional[int] = None
    employer: Optional[str] = None
    bio: Optional[str] = None
    signup_period: Optional[str] = None


class UserRead(BaseModel):
    id: int
    email: str
    role: RoleEnum
    first_name: Optional[str]
    last_name: Optional[str]
    oa_id: Optional[str]
    lodge_id: Optional[str]
    chapter: Optional[str]
    region: Optional[str]
    industry: Optional[str]
    graduation_year: Optional[int]
    employer: Optional[str]
    bio: Optional[str]
    signup_period: Optional[str]
    is_active: bool
    created_at: Optional[datetime]

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    token: str
    user: UserRead
