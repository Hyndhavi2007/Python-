employees = {
    "E001": {
        "Name": "Sheldon Cooper",
        "Department": "HR",
        "Salary": 500000
    },
    "E002": {
        "Name": "Shaun Murphy",
        "Department": "IT",
        "Salary": 650000
    }
}

for employee_id, employee_data in employees.items():
    print(f"{employee_id}: {employee_data['Name']} - {employee_data['Department']}")

for employee_data in employees.values():
    employee_data["Experience"] = 0

print(employees)