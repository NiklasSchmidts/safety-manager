from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    position: str
    department: str


class EmployeeRead(EmployeeCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None
