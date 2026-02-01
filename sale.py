class Sale:
    """
    Represents a sale transaction in the store.
    """

    def __init__(
        self,
        id: str,
        name: str,
        quantity: int,
        total_price: float,
        staff_username: str,
        date: str,
    ) -> None:
        self.id = id
        self.name = name
        self.staff_username = staff_username
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("Sale id cannot be empty")
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
    def staff_username(self) -> str:
        return self._staff_username

    @staff_username.setter
    def staff_username(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("Staff username cannot be empty")
        self._staff_username = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        value = int(value)
        if value <= 0:
            raise ValueError("Quantity must be positive")
        self._quantity = value

    @property
    def total_price(self) -> float:
        return self._total_price

    @total_price.setter
    def total_price(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("Total price cannot be negative")
        self._total_price = value

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, value: str) -> None:
        self._date = str(value)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "staff_username": self.staff_username,
            "date": self.date,
        }
