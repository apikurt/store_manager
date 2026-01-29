import json
from pathlib import Path

from staff import Staff

username = input("Enter Staff Username: ").strip()
role = input("Enter Staff Role: ").strip()
password = input("Enter Staff Password: ").strip()

existing_data = {}

if Path("db.json").exists():
    with Path("db.json").open("r", encoding="utf-8") as f:
        try:
            existing_data = json.load(f)
            existing_staff = existing_data.get("staff", [])
        except json.JSONDecodeError:
            existing_staff = []
else:
    existing_staff = []

employee_id = f"EMP{len(existing_staff) + 1:03d}"

new_staff = Staff(
    username=username,
    employee_id=employee_id,
    role=role,
    password=password,
)

existing_staff.append(new_staff.to_dict())

with Path("db.json").open("w", encoding="utf-8") as f:
    json.dump(
        {
            "products": existing_data.get("products", []),
            "staff": existing_staff,
            "sales": existing_data.get("sales", []),
        },
        f,
        indent=2,
        ensure_ascii=False,
    )
