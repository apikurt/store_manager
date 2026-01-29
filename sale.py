class Sale:
    """
    Represents a sale transaction in the store.
    """

    def __init__(self, product_id: str, quantity: int, total_price: float, date: str):
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "date": self.date,
        }