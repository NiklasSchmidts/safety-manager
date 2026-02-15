from datetime import datetime
from typing import TYPE_CHECKING, Optional

from core.database import Base
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.equipment import Equipment  # noqa: F401


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    position: Mapped[str] = mapped_column(nullable=False)
    department: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    equipments: Mapped[list["Equipment"]] = relationship(
        "Equipment", back_populates="assigned_employee"
    )

    def __repr__(self) -> str:
        return f"<Employee(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})>"
