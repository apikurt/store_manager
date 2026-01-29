from typing import Literal

from product import Product


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
        self.category = "Cleaning Supplies"
        self.material_state = material_state

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "material_state": self.material_state,
        }
