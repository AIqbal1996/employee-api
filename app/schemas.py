from pydantic import BaseModel, Field, EmailStr


class Employee(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18, le=100)
    department: str
    salary: float = Field(..., gt=0)


class EmployeeResponse(Employee):
    id: int