from schemas.employee import EmployeeCreate, EmployeeRead
from sqlalchemy.ext.asyncio import AsyncSession

import app.crud.employee as crud


async def get_employees(session: AsyncSession) -> list[EmployeeRead]:
    return await crud.get_employees(session)


async def create_employee(
    employee: EmployeeCreate, session: AsyncSession
) -> EmployeeRead:
    return await crud.create_employee(employee, session)


async def update_employee(
    employee_id: int, employee: EmployeeCreate, session: AsyncSession
) -> EmployeeRead:
    return await crud.update_employee(employee_id, employee, session)


async def delete_employee(employee_id: int, session: AsyncSession) -> None:
    await crud.delete_employee(employee_id, session)
