from .base import MenuBase


class ViewInventoryMenu(MenuBase):
    def __init__(self, data_manager):
        super().__init__(data_manager)

    def run(self):
        self.clear_screen()

        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        print("--- Inventory ---")
        inventory = self.data_manager.load_data().get("products", [])
        if not inventory:
            print("No products in inventory.")
        else:
            print(
                f"{'Product Name':<20} {'Price':<10} {'Price w/ Tax':<15} {'Stock':<10}"
            )
            print("-" * 60)
            for product in inventory:
                print(
                    f"{product.name:<20} €{product.price:<10.2f} €{product.price + product.calculate_tax():<15.2f} {product.stock:<10}"
                )
        print()
        input("Press Enter to return to the Inventory Management Menu...")
        from .manage_inventory import ManageInventoryMenu

        return ManageInventoryMenu(self.data_manager)
