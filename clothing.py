from typing import Any, Dict

from product import Product


class Clothing(Product):
    def __init__(
        self,
        name: str,
        price: float,
        stock: int,
        size: str,
        material: str,
    ) -> None:
        super().__init__(name=name, price=price, stock=stock)
        self.category = "clothing"
        self._size = size.strip()
        self._material = material.strip()
        self.tax_rate = 0.12  # 12% VAT for clothing

    @property
    def size(self) -> str:
        return self._size

    @property
    def material(self) -> str:
        return self._material

    def calculate_tax(self) -> float:
        unit_price = self.price
        return round(unit_price * self.tax_rate, 2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "category": self.category,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "size": self.size,
            "material": self.material,
        }
