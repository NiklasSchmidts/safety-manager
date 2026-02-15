from typing import Sequence

from models.employee import Employee
from schemas.employee import EmployeeCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_employees(session: AsyncSession) -> Sequence[Employee]:
    query = select(Employee)
    result = await session.execute(query)
    return result.scalars().all()


async def create_employee(employee: EmployeeCreate, session: AsyncSession) -> Employee:
    new_employee = Employee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email,
        position=employee.position,
        department=employee.department,
    )
    session.add(new_employee)
    await session.commit()
    await session.refresh(new_employee)
    return new_employee


async def update_employee(
    employee_id: int, employee: EmployeeCreate, session: AsyncSession
) -> Employee:
    query = select(Employee).where(Employee.id == employee_id)
    result = await session.execute(query)
    existing_employee = result.scalar_one_or_none()

    if not existing_employee:
        raise ValueError(f"Employee with id {employee_id} not found")

    existing_employee.first_name = employee.first_name
    existing_employee.last_name = employee.last_name
    existing_employee.email = employee.email
    existing_employee.position = employee.position
    existing_employee.department = employee.department

    session.add(existing_employee)
    await session.commit()
    await session.refresh(existing_employee)
    return existing_employee


async def delete_employee(employee_id: int, session: AsyncSession) -> None:
    query = select(Employee).where(Employee.id == employee_id)
    result = await session.execute(query)
    existing_employee = result.scalar_one_or_none()

    if not existing_employee:
        raise ValueError(f"Employee with id {employee_id} not found")

    await session.delete(existing_employee)
    await session.commit()
