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
        self.id = str(id).strip()
        self.name = str(name).strip()
        self.staff_username = str(staff_username).strip()
        self.quantity = int(quantity)
        self.total_price = float(total_price)
        self.date = date

        if not self.id:
            raise ValueError("Sale id cannot be empty")
        if not self.name:
            raise ValueError("Product name cannot be empty")
        if not self.staff_username:
            raise ValueError("Staff username cannot be empty")
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.total_price < 0:
            raise ValueError("Total price cannot be negative")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "staff_username": self.staff_username,
            "date": self.date,
        }
