import json
from pathlib import Path
from typing import Any

from cleaning_supplies import CleaningSupplies
from clothing import Clothing
from electronics import Electronics
from sale import Sale
from staff import Manager, Staff, Worker


class DataManager:
    # --- Initialization ---
    def __init__(self, inventory_path: str | Path = "db.json") -> None:
        self._path = Path(inventory_path)
        self.current_staff: Staff | None = None

    # --- Persistence ---
    @staticmethod
    def _empty_data() -> dict[str, Any]:
        return {"products": [], "staff": [], "sales": []}

    def load_data(self) -> dict[str, Any]:
        if not self._path.exists():
            data = self._empty_data()
            self.save_data(data)
            return data

        try:
            raw = json.loads(self._path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return self._empty_data()

        if not isinstance(raw, dict):
            return self._empty_data()

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

    def _append_and_save(self, key: str, item: Any) -> None:
        if item is None:
            return
        current_data = self.load_data()
        items = current_data.get(key, [])
        items.append(item)
        current_data[key] = items
        self.save_data(current_data)

    # --- Deserialization ---
    def product_from_dict(
        self, data: dict[str, Any]
    ) -> Clothing | Electronics | CleaningSupplies | None:
        category = str(data.get("category", "")).strip()

        try:
            product_id = str(data["id"]).strip()
            name = str(data["name"])
            price = float(data["price"])
            stock = int(data["stock"])
        except (KeyError, TypeError, ValueError):
            return None

        if category == "Electronics":
            try:
                warranty_months = int(data.get("warranty_months", 0))
            except (TypeError, ValueError):
                warranty_months = 0
            try:
                return Electronics(
                    product_id=product_id,
                    name=name,
                    price=price,
                    stock=stock,
                    warranty_months=warranty_months,
                )
            except ValueError:
                return None

        if category == "Clothing":
            size = str(data.get("size", ""))
            material = str(data.get("material", ""))
            try:
                return Clothing(
                    product_id=product_id,
                    name=name,
                    price=price,
                    stock=stock,
                    size=size,
                    material=material,
                )
            except ValueError:
                return None

        if category == "Cleaning Supplies":
            material_state = str(data.get("material_state", "liquid"))
            try:
                return CleaningSupplies(
                    product_id=product_id,
                    name=name,
                    price=price,
                    stock=stock,
                    material_state=material_state,
                )
            except ValueError:
                return None
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
            role_key = role.strip().lower()
            if role_key == "manager":
                return Manager(
                    username=username,
                    employee_id=employee_id,
                    password=password,
                )
            if role_key == "worker":
                return Worker(
                    username=username,
                    employee_id=employee_id,
                    password=password,
                )
            return None
        except ValueError:
            return None

    def sale_from_dict(self, data: dict[str, Any]) -> Sale | None:
        try:
            sale_id = str(data["id"]).strip()
            product_name = str(data["name"]).strip()
            quantity = int(data["quantity"])
            total_price = float(data["total_price"])
            staff_username = str(data["staff_username"]).strip()
            date = str(data["date"]).strip()
        except (KeyError, TypeError, ValueError):
            return None

        try:
            return Sale(
                id=sale_id,
                name=product_name,
                quantity=quantity,
                total_price=total_price,
                staff_username=staff_username,
                date=date,
            )
        except ValueError:
            return None

    # --- Creation ---
    def add_new_product(
        self, product: Clothing | Electronics | CleaningSupplies
    ) -> None:
        self._append_and_save("products", product)

    def add_new_staff(self, staff_member: Staff) -> None:
        self._append_and_save("staff", staff_member)

    def add_new_sale(self, sale: Sale) -> None:
        self._append_and_save("sales", sale)

    # --- Authentication ---
    def login_staff(self, username: str, password: str) -> Staff | None:
        current_data = self.load_data()
        for staff_member in current_data.get("staff", []):
            if staff_member.username == username and staff_member._password == password:
                self.current_staff = staff_member
                return staff_member
        return None

    # --- Inventory operations ---
    def load_inventory(self) -> list[Clothing | Electronics | CleaningSupplies]:
        data = self.load_data()
        return data.get("products", [])

    def next_product_id(self) -> str:
        max_id = 0
        for product in self.load_data().get("products", []):
            raw_id = product.id.strip()
            raw_id = raw_id[3:] if raw_id.upper().startswith("PRD") else raw_id
            try:
                max_id = max(max_id, int(raw_id))
            except ValueError:
                continue
        return f"PRD{max_id + 1:04d}"

    def remove_product(
        self, product: Clothing | Electronics | CleaningSupplies
    ) -> None:
        current_data = self.load_data()
        products = current_data.get("products", [])
        products = [p for p in products if p.id != product.id]
        current_data["products"] = products
        self.save_data(current_data)

    def update_product(
        self, product: Clothing | Electronics | CleaningSupplies
    ) -> None:
        current_data = self.load_data()
        products = current_data.get("products", [])
        updated_products = []
        for p in products:
            if p.id == product.id:
                updated_products.append(product)
            else:
                updated_products.append(p)
        current_data["products"] = updated_products
        self.save_data(current_data)
