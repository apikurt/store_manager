# Utility script to create a new staff member and add to db.json
# Not a part of the main application

import json
from pathlib import Path

from staff import Manager, Worker

username = input("Enter Staff Username: ").strip()
print("Select Role:")
print("1. Worker (default)")
print("2. Manager")
role_choice = input("Select an option: ").strip()
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

max_id = 0
for staff in existing_staff:
    raw_id = str(staff.get("employee_id", "")).strip()
    if raw_id.upper().startswith("EMP"):
        raw_id = raw_id[3:]
    try:
        max_id = max(max_id, int(raw_id))
    except ValueError:
        continue
employee_id = f"EMP{max_id + 1:03d}"

if role_choice == "2":
    new_staff = Manager(
        username=username,
        employee_id=employee_id,
        password=password,
    )
else:
    new_staff = Worker(
        username=username,
        employee_id=employee_id,
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
