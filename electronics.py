from product import Product


class Electronics(Product):
    def __init__(
        self,
        name: str,
        price: float,
        stock: int,
        warranty_months: int,
    ) -> None:
        super().__init__(name=name, price=price, stock=stock)
        self.category = "electronics"
        warranty_months = int(warranty_months)
        if warranty_months < 0:
            raise ValueError("Warranty months cannot be negative")
        self._warranty_months = warranty_months
        self.tax_rate = 0.20  # 20% VAT for electronics

    @property
    def warranty_months(self) -> int:
        return self._warranty_months

    def calculate_tax(self) -> float:
        unit_price = self.price
        return round(unit_price * self.tax_rate, 2)

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "warranty_months": self.warranty_months,
        }
