from product import Product


class Electronics(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        warranty_months: int,
    ) -> None:
        super().__init__(product_id=product_id, name=name, price=price, stock=stock)
        self.category = "Electronics"
        warranty_months = int(warranty_months)
        if warranty_months < 0:
            raise ValueError("Warranty months cannot be negative")
        self._warranty_months = warranty_months
        self.tax_rate = 0.20  # 20% VAT for electronics

    @property
    def warranty_months(self) -> int:
        return self._warranty_months

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "warranty_months": self.warranty_months,
        }
