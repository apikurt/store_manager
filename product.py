from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int) -> None:
        self._id = str(product_id).strip()
        if not self._id:
            raise ValueError("Product id cannot be empty")
        self._name = name.strip()
        self.tax_rate = 0.0  # tax rate will be overridden by subclasses
        self.price = price
        self.stock = stock

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @price.setter
    def price(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = round(value, 2)

    @stock.setter
    def stock(self, value: int) -> None:
        value = int(value)
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = value

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
