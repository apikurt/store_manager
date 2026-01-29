from .base import MenuBase
from .login import LoginMenu


class MainMenu(MenuBase):
    def run(self):
        if not self.data_manager.current_staff:
            return LoginMenu(self.data_manager)

        self.show_header("Main Menu")
        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        print("Options:")
        print("1. Manage Inventory")
        print("2. Process Sales")
        print("3. Exit")
        print()
        choice = input("Select an option: ").strip()

        if choice == "1":
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)
        elif choice == "2":
            pass  # Transition to Sales Processing Menu
        elif choice == "3":
            self.exit_application()
        else:
            print()
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
            return self  # Stay in the main menu
