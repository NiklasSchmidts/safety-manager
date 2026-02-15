from datetime import datetime
from typing import TYPE_CHECKING, Optional

from core.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.employee import Employee  # noqa: F401


class Equipment(Base):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped["EquipmentType"] = relationship("EquipmentType")
    type_id: Mapped[int] = mapped_column(ForeignKey("equipment_types.id"))
    serial_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    purchase_date: Mapped[datetime] = mapped_column(nullable=False)
    last_maintenance_date: Mapped[datetime] = mapped_column(nullable=False)
    is_operational: Mapped[bool] = mapped_column(nullable=False, default=True)
    assigned_employee_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employees.id"), nullable=True
    )
    assigned_employee: Mapped["Employee"] = relationship(
        "Employee", back_populates="equipments"
    )

    def __repr__(self) -> str:
        return f"<Equipment(id={self.id}, name={self.name}, type={self.type})>"


class EquipmentType(Base):
    __tablename__ = "equipment_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type_name: Mapped[str] = mapped_column(nullable=False, unique=True)
