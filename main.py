from fastapi import FastAPI, Depends, HTTPException, status

from app.schemas import Employee
from app.auth import verify_api_key

from app.crud import (
    create_employee,
    get_employees,
    get_employee,
    update_employee,
    delete_employee
)


app = FastAPI(
    title="Employee Management API",
    description="API Key Protected Employee API",
    version="1.0.0"
)


@app.get("/employees")
def get_all_employees(
    api_key: str = Depends(verify_api_key)
):
    return get_employees()


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def add_employee(
    employee: Employee,
    api_key: str = Depends(verify_api_key)
):
    return create_employee(employee)


@app.get("/employees/{employee_id}")
def get_single_employee(
    employee_id: int,
    api_key: str = Depends(verify_api_key)
):

    employee = get_employee(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@app.put("/employees/{employee_id}")
def update_existing_employee(
    employee_id: int,
    employee: Employee,
    api_key: str = Depends(verify_api_key)
):

    updated_employee = update_employee(
        employee_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


@app.delete("/employees/{employee_id}")
def remove_employee(
    employee_id: int,
    api_key: str = Depends(verify_api_key)
):

    deleted_employee = delete_employee(employee_id)

    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee": deleted_employee
    }