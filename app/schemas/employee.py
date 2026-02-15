from datetime import datetime

from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    position: str
    department: str


class EmployeeRead(EmployeeCreate):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True
