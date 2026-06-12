import enum
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class MatchStatusEnum(str, enum.Enum):
    pending = "pending"
    active = "active"
    completed = "completed"


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mentor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    signup_period = Column(String(20), nullable=False)
    match_score = Column(Float)
    match_criteria = Column(JSONB)
    status = Column(Enum(MatchStatusEnum), default=MatchStatusEnum.pending)
    matched_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("User", foreign_keys=[student_id])
    mentor = relationship("User", foreign_keys=[mentor_id])
