from .base import MenuBase


class RemoveProductMenu(MenuBase):
    def run(self):
        self.show_header("Remove Product")
        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        inventory = self.data_manager.load_data().get("products", [])
        if not inventory:
            print("No products in inventory to remove.")
            input("Press Enter to return to the Inventory Management Menu...")
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)

        print("Products:")
        for idx, product in enumerate(inventory, start=1):
            print(f"{idx}. {product.name} (Stock: {product.stock})")
        print()
        choice = input(
            "Enter the number of the product to remove (or 'b' to go back): "
        ).strip()

        if choice.lower() == "b":
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)

        try:
            product_index = int(choice) - 1
            if 0 <= product_index < len(inventory):
                product_to_remove = inventory[product_index]
                self.data_manager.remove_product(product_to_remove)
                print()
                print(f"Product '{product_to_remove.name}' has been removed.")
            else:
                print()
                print("Invalid product number.")
        except ValueError:
            print()
            print("Invalid input. Please enter a valid number.")

        input("Press Enter to return to the Inventory Management Menu...")
        from .manage_inventory import ManageInventoryMenu

        return ManageInventoryMenu(self.data_manager)
