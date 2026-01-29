import json
from pathlib import Path
from typing import Any
from datetime import datetime

from clothing import Clothing
from electronics import Electronics
from cleaning_supplies import CleaningSupplies

from staff import Staff
from sale import Sale


class DataManager:
    def __init__(self, inventory_path: str | Path = "db.json") -> None:
        self._path = Path(inventory_path)
        self.current_staff: Staff | None = None

    def load_data(self) -> dict[str, Any]:
        if not self._path.exists():
            with self._path.open("w", encoding="utf-8") as f:
                json.dump({"products": [], "staff": [], "sales": []}, f)
            return {"products": [], "staff": [], "sales": []}

        try:
            raw = json.loads(self._path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"products": [], "staff": [], "sales": []}

        if not isinstance(raw, dict):
            return {"products": [], "staff": [], "sales": []}

        products: list[Clothing | Electronics | CleaningSupplies] = []
        for item in raw.get("products", []):
            if not isinstance(item, dict):
                continue
            product = self.product_from_dict(item)
            if product is not None:
                products.append(product)
        staff: list[Staff] = []
        for item in raw.get("staff", []):
            if not isinstance(item, dict):
                continue
            staff_member = self.staff_from_dict(item)
            if staff_member is not None:
                staff.append(staff_member)
        sales: list[Sale] = []
        for item in raw.get("sales", []):
            if not isinstance(item, dict):
                continue
            sale_entry = self.sale_from_dict(item)
            if sale_entry is not None:
                sales.append(sale_entry)
        return {"products": products, "staff": staff, "sales": sales}

    def save_data(self, data: dict[str, Any]) -> None:
        to_save = {
            "products": [p.to_dict() for p in data.get("products", [])],
            "staff": [s.to_dict() for s in data.get("staff", [])],
            "sales": [s.to_dict() for s in data.get("sales", [])],
        }
        with self._path.open("w", encoding="utf-8") as f:
            json.dump(to_save, f, indent=2, ensure_ascii=False)

    def product_from_dict(
        self, data: dict[str, Any]
    ) -> Clothing | Electronics | CleaningSupplies | None:
        category = str(data.get("category", "")).lower()

        try:
            name = str(data["name"])
            price = float(data["price"])
            stock = int(data["stock"])
        except (KeyError, TypeError, ValueError):
            return None

        if category == "electronics":
            try:
                warranty_months = int(data.get("warranty_months", 0))
            except (TypeError, ValueError):
                warranty_months = 0
            try:
                return Electronics(
                    name=name,
                    price=price,
                    stock=stock,
                    warranty_months=warranty_months,
                )
            except ValueError:
                return None

        if category == "clothing":
            size = str(data.get("size", ""))
            material = str(data.get("material", ""))
            try:
                return Clothing(
                    name=name,
                    price=price,
                    stock=stock,
                    size=size,
                    material=material,
                )
            except ValueError:
                return None

        if category == "cleaning_supplies":
            material_state = str(data.get("material_state", "liquid"))
            try:
                return CleaningSupplies(
                    name=name,
                    price=price,
                    stock=stock,
                    material_state=material_state,
                )
            except ValueError:
                return None

    def staff_from_dict(self, data: dict[str, Any]) -> Staff | None:
        try:
            username = str(data["username"])
            employee_id = str(data["employee_id"])
            role = str(data["role"])
            password = str(data["password"])
        except (KeyError, TypeError, ValueError):
            return None

        try:
            return Staff(
                username=username,
                employee_id=employee_id,
                role=role,
                password=password,
            )
        except ValueError:
            return None

    def sale_from_dict(self, data: dict[str, Any]) -> Sale | None:
        try:
            product_name = str(data["product_name"])
            sold_by = str(data["sold_by"])
            staff_username = str(data["staff_username"])
        except (KeyError, TypeError, ValueError):
            return None

        try:
            now = datetime.now()
            return Sale(
                product_name=product_name,
                sold_by=sold_by,
                staff_username=staff_username,
                date=now.strftime("%Y-%m-%d %H:%M:%S"),
            )
        except ValueError:
            return None

    def add_new_product(
        self, product: Clothing | Electronics | CleaningSupplies
    ) -> None:
        current_data = self.load_data()
        products_list = current_data.get("products", [])
        products_list.append(product)
        current_data["products"] = products_list
        self.save_data(current_data)

    def add_new_staff(self, staff_member: Staff) -> None:
        current_data = self.load_data()
        staff_list = current_data.get("staff", [])
        staff_list.append(staff_member)
        current_data["staff"] = staff_list
        self.save_data(current_data)

    def add_new_sale(self, sale: Sale) -> None:
        current_data = self.load_data()
        sales_list = current_data.get("sales", [])
        sales_list.append(sale)
        current_data["sales"] = sales_list
        self.save_data(current_data)

    def login_staff(self, username: str, password: str) -> Staff | None:
        current_data = self.load_data()
        for staff_member in current_data.get("staff", []):
            if staff_member.username == username and staff_member._password == password:
                self.current_staff = staff_member
                return staff_member
        return None

    def load_inventory(self) -> list[Clothing | Electronics | CleaningSupplies]:
        data = self.load_data()
        return data.get("products", [])
