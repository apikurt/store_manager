from .base import MenuBase


class UpdateProductMenu(MenuBase):
    def run(self):
        self.show_header("Update Product")
        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        inventory = self.data_manager.load_data().get("products", [])
        if not inventory:
            print("No products in inventory to update.")
            input("Press Enter to return to the Inventory Management Menu...")
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)

        print("Products:")
        for idx, product in enumerate(inventory, start=1):
            print(
                f"{idx}. {product.name} (Stock: {product.stock}, Price: {product.price:.2f} EUR)"
            )
        print()
        choice = input(
            "Enter the number of the product to update (or 'b' to go back): "
        ).strip()

        if choice.lower() == "b":
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)

        try:
            product_index = int(choice) - 1
            if 0 <= product_index < len(inventory):
                print('Leaving fields blank will keep current values.')
                print()
                product_to_update = inventory[product_index]
                new_price = input(
                    f"Enter new price for '{product_to_update.name}' (current: {product_to_update.price:.2f} EUR): "
                ).strip()
                new_stock = input(
                    f"Enter new stock for '{product_to_update.name}' (current: {product_to_update.stock}): "
                ).strip()

                changed = False
                if new_price:
                    product_to_update.price = float(new_price)
                    changed = True
                if new_stock:
                    product_to_update.stock = int(new_stock)
                    changed = True

                if changed:
                    self.data_manager.update_product(product_to_update)
                    print()
                    print(f"Product '{product_to_update.name}' has been updated.")
                else:
                    print()
                    print("No changes entered. Product not updated.")
            else:
                print()
                print("Invalid product number.")
        except ValueError:
            print()
            print("Invalid input. Please enter valid numbers.")

        input("Press Enter to return to the Inventory Management Menu...")
        from .manage_inventory import ManageInventoryMenu

        return ManageInventoryMenu(self.data_manager)
