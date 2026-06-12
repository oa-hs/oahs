from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel
from app.models.match import MatchStatusEnum
from app.schemas.user import UserRead


class MatchRead(BaseModel):
    id: int
    student_id: int
    mentor_id: int
    signup_period: str
    match_score: Optional[float]
    match_criteria: Optional[Any]
    status: MatchStatusEnum
    matched_at: Optional[datetime]
    student: Optional[UserRead] = None
    mentor: Optional[UserRead] = None

    model_config = {"from_attributes": True}


class RunMatchingRequest(BaseModel):
    signup_period: str
