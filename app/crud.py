employees = []


def create_employee(employee):
    new_employee = {
        "id": len(employees) + 1,
        "name": employee.name,
        "email": employee.email,
        "age": employee.age,
        "department": employee.department,
        "salary": employee.salary
    }

    employees.append(new_employee)

    return new_employee


def get_employees():
    return employees


def get_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None


def update_employee(employee_id, employee):
    for existing_employee in employees:

        if existing_employee["id"] == employee_id:

            existing_employee["name"] = employee.name
            existing_employee["email"] = employee.email
            existing_employee["age"] = employee.age
            existing_employee["department"] = employee.department
            existing_employee["salary"] = employee.salary

            return existing_employee

    return None


def delete_employee(employee_id):
    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return employee

    return None