import crud.employee as crud
from core.database import get_session
from fastapi import APIRouter, Depends, status
from schemas.employee import EmployeeCreate, EmployeeRead
from sqlalchemy.ext.asyncio import AsyncSession


def create_employee_router():
    router = APIRouter()

    @router.get("/", response_model=list[EmployeeRead], status_code=status.HTTP_200_OK)
    async def get_employees(session: AsyncSession = Depends(get_session)):
        employees = await crud.get_employees(session)
        return employees

    @router.post("/", response_model=EmployeeRead, status_code=status.HTTP_201_CREATED)
    async def create_employee(
        employee: EmployeeCreate, session: AsyncSession = Depends(get_session)
    ):
        return await crud.create_employee(employee, session)

    @router.patch(
        "/{employee_id}", response_model=EmployeeRead, status_code=status.HTTP_200_OK
    )
    async def update_employee(
        employee_id: int,
        employee: EmployeeCreate,
        session: AsyncSession = Depends(get_session),
    ):
        return await crud.update_employee(employee_id, employee, session)

    @router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_employee(
        employee_id: int, session: AsyncSession = Depends(get_session)
    ):
        await crud.delete_employee(employee_id, session)
        return None

    return router
