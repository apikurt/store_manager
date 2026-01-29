from .base import MenuBase
from .login import LoginMenu


class MainMenu(MenuBase):
    def __init__(self, data_manager):
        super().__init__(data_manager)

    def run(self):
        self.clear_screen()

        print("=== Store Manager Main Menu ===")
        print()

        if not self.data_manager.current_staff:
            return LoginMenu(self.data_manager)

        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        print("--- Main Menu ---")
        print("1. Manage Inventory")
        print("2. Process Sales")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)
        elif choice == "2":
            pass  # Transition to Sales Processing Menu
        elif choice == "3":
            return None  # Exit the system
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
            return self  # Stay in the main menu
