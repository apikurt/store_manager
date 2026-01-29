from .base import MenuBase


class ManageInventoryMenu(MenuBase):
    def run(self):
        self.show_header("Inventory Management")
        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        print("Options:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. View Inventory")
        print("5. Return to Main Menu")
        print("6. Exit Application")
        print()
        choice = input("Select an option: ").strip()

        if choice == "1":
            from .add_product import AddProductMenu

            return AddProductMenu(self.data_manager)
        elif choice == "2":
            from .remove_product import RemoveProductMenu

            return RemoveProductMenu(self.data_manager)
        elif choice == "3":
            pass  # Logic to update product
        elif choice == "4":
            from .view_inventory import ViewInventoryMenu

            return ViewInventoryMenu(self.data_manager)
        elif choice == "5":
            from .main_menu import MainMenu

            return MainMenu(self.data_manager)
        elif choice == "6":
            self.exit_application()
        else:
            print()
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
            return self  # Stay in the inventory management menu
