from .base import MenuBase


class ListRecentSalesMenu(MenuBase):
    def run(self):
        self.show_header("Recent Sales")
        self.show_user()

        sales = self.data_manager.load_data().get("sales", [])
        if not sales:
            print("No recent sales found.")
        else:
            print("Recent Sales:")
            print()
            print(
                f"{'Sale ID':<20} {'Product Name':<22} {'Qty':>5} {'Total (EUR)':>14} {'Staff':<12} {'Date':<19}"
            )
            print("-" * 98)
            for sale in sales[-10:]:  # Show last 10 sales
                print(
                    f"{sale.id:<20} {sale.name:<22} {sale.quantity:>5} {sale.total_price:>14.2f} {sale.staff_username:<12} {sale.date:<19}"
                )
        print()
        input("Press Enter to return to the Main Menu...")
        from .main_menu import MainMenu

        return MainMenu(self.data_manager)
