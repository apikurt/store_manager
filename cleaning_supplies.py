from product import Product
from typing import Literal


class CleaningSupplies(Product):
    def __init__(
        self,
        name: str,
        price: float,
        stock: int,
        material_state: Literal["liquid", "solid", "gas"] = "liquid",
    ) -> None:
        super().__init__(name=name, price=price, stock=stock)
        self.tax_rate = 0.15  # 15% VAT for cleaning supplies
        self.category = "cleaning_supplies"
        self.material_state = material_state

    def calculate_tax(self) -> float:
        unit_price = self.price
        return round(unit_price * self.tax_rate, 2)

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "material_state": self.material_state,
        }
