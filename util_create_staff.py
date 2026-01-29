from storemanager.staff import Staff
import json
from pathlib import Path

name = input("Enter Staff Name: ").strip()
position = input("Enter Staff Position: ").strip()
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
    name=name,
    employee_id=employee_id,
    role=position,
    password=password,
)

existing_staff.append(new_staff.to_dict())

with Path("db.json").open("w", encoding="utf-8") as f:
    json.dump(
        {"products": existing_data.get("products", []), "staff": existing_staff},
        f,
        indent=2,
        ensure_ascii=False,
    )
