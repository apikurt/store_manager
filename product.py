from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
    ) -> None:
        self.id = str(product_id).strip()
        self.name = name.strip()
        self.price = price
        self.stock = stock
        self.tax_rate = 0.0  # tax rate will be overridden by subclasses
        self.category = ""  # category will be set by subclasses

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("Product id cannot be empty")
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("Product name cannot be empty")
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round(value, 2)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        value = int(value)
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value

    @property
    def tax_rate(self) -> float:
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("Tax rate cannot be negative")
        self._tax_rate = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str) -> None:
        self._category = str(value)

    def remove_stock(self, quantity: int) -> None:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.stock:
            raise ValueError("Insufficient stock")
        self.stock = self.stock - quantity

    def calculate_tax(self) -> float:
        return round(self.price * self.tax_rate, 2)

    @abstractmethod
    def to_dict(self) -> dict:
        pass
