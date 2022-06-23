from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class GoalBase(SQLModel):
    name: str
    description: Optional[str]
    current_value: float = 0
    desired_value: float
    unit: str
    is_starred: bool = False
    created_at: Optional[datetime]
    last_edited: Optional[datetime]


class Goal(GoalBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    last_edited: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class GoalCreate(GoalBase):
    pass


class GoalProgressBase(SQLModel):
    current_value: float


class GoalProgress(GoalProgressBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)


class GoalProgressCreate(GoalProgressBase):
    pass
