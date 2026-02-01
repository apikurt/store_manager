from typing import Literal

from product import Product


class CleaningSupplies(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        material_state: Literal["liquid", "solid", "gas"] = "liquid",
    ) -> None:
        super().__init__(product_id=product_id, name=name, price=price, stock=stock)
        self.tax_rate = 0.15  # 15% VAT for cleaning supplies
        self.category = "Cleaning Supplies"
        self.material_state = material_state

    @property
    def material_state(self) -> str:
        return self._material_state

    @material_state.setter
    def material_state(self, value: str) -> None:
        if value not in ["liquid", "solid", "gas"]:
            raise ValueError("material_state must be 'liquid', 'solid', or 'gas'")
        self._material_state = str(value)

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "material_state": self.material_state,
        }
