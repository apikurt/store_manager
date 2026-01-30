from .base import MenuBase


class ViewInventoryMenu(MenuBase):
    def run(self):
        self.show_header("Inventory")
        self.show_user()

        inventory = self.data_manager.load_data().get("products", [])
        if not inventory:
            print("No products in inventory.")
        else:
            print("Items:")
            print()
            print(
                f"{'ID':<10} {'Product Name':<20} {'Price (EUR)':>14} {'Price w/ Tax (EUR)':>20} {'Stock':>8}"
            )
            print("-" * 80)
            for product in inventory:
                print(
                    f"{product.id:<10} {product.name:<20} {product.price:>14.2f} {product.price + product.calculate_tax():>20.2f} {product.stock:>8}"
                )
        print()
        input("Press Enter to return to the Inventory Management Menu...")
        from .manage_inventory import ManageInventoryMenu

        return ManageInventoryMenu(self.data_manager)
