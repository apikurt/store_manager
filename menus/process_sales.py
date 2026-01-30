from datetime import datetime

from .base import MenuBase


class ProcessSalesMenu(MenuBase):
    def run(self):
        from .main_menu import MainMenu

        self.show_header("Process Sales")
        self.show_user()

        inventory = self.data_manager.load_data().get("products", [])
        if not inventory:
            print("No products available to sell.")
            input("Press Enter to return to the Main Menu...")
            return MainMenu(self.data_manager)

        print("Products:")
        for idx, product in enumerate(inventory, start=1):
            price_with_tax = product.price + product.calculate_tax()
            print(
                f"{idx}. {product.name} (Stock: {product.stock}, Price w/ Tax: {price_with_tax:.2f} EUR)"
            )
        print()
        choice = input("Enter product number to sell (or 'b' to go back): ").strip()

        if choice.lower() == "b":
            return MainMenu(self.data_manager)

        try:
            product_index = int(choice) - 1
            if not 0 <= product_index < len(inventory):
                print()
                print("Invalid product number.")
                input("Press Enter to return to the Main Menu...")
                return MainMenu(self.data_manager)

            product_to_sell = inventory[product_index]
            quantity_input = input(
                f"Enter quantity for '{product_to_sell.name}' (available: {product_to_sell.stock}): "
            ).strip()
            quantity = int(quantity_input)
            if quantity <= 0 or quantity > product_to_sell.stock:
                print()
                print("Invalid quantity.")
                input("Press Enter to return to the Main Menu...")
                return MainMenu(self.data_manager)

            unit_total = product_to_sell.price + product_to_sell.calculate_tax()
            total_price = unit_total * quantity

            print()
            print("Sale Summary:")
            print(f"{quantity} x {product_to_sell.name} @ {unit_total:.2f} EUR each")
            print(f"Total: {total_price:.2f} EUR")
            print()
            confirm = input("Confirm sale? (y/N): ").strip().lower()
            if confirm != "y":
                print()
                print("Sale cancelled.")
                input("Press Enter to return to the Main Menu...")
                return MainMenu(self.data_manager)

            sale_id = f"SALE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            sale = self.data_manager.sale_from_dict(
                {
                    "id": sale_id,
                    "name": product_to_sell.name,
                    "quantity": quantity,
                    "total_price": total_price,
                    "staff_username": self.data_manager.current_staff.username,
                    "date": sale_date,
                }
            )
            self.data_manager.add_new_sale(sale)

            product_to_sell.remove_stock(quantity)
            self.data_manager.update_product(product_to_sell)

            print()
            print(
                f"Sale recorded. Total: {total_price:.2f} EUR for {quantity} x {product_to_sell.name}."
            )
        except ValueError:
            print()
            print("Invalid input. Please enter valid numbers.")

        input("Press Enter to return to the Main Menu...")
        return MainMenu(self.data_manager)
