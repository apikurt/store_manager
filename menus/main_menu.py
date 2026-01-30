from .base import MenuBase


class MainMenu(MenuBase):
    def run(self):
        if not self.data_manager.current_staff:
            from .login import LoginMenu

            return LoginMenu(self.data_manager)

        self.show_header("Main Menu")
        self.show_user()

        print("Options:")
        print("1. Manage Inventory")
        print("2. Process Sales")
        print("3. List Recent Sales")
        is_manager = self.data_manager.current_staff.role == "manager"
        if is_manager:
            print("4. Manage Staff")
            print("5. Exit Application")
        else:
            print("4. Exit Application")
        print()
        choice = input("Select an option: ").strip()

        if choice == "1":
            from .manage_inventory import ManageInventoryMenu

            return ManageInventoryMenu(self.data_manager)
        elif choice == "2":
            from .process_sales import ProcessSalesMenu

            return ProcessSalesMenu(self.data_manager)
        elif choice == "3":
            from .recent_sales import ListRecentSalesMenu

            return ListRecentSalesMenu(self.data_manager)
        elif choice == "4":
            if is_manager:
                from .manage_staff import ManageStaffMenu

                return ManageStaffMenu(self.data_manager)
            self.exit_application()
        elif choice == "5":
            if is_manager:
                self.exit_application()
            else:
                print()
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
                return self
        else:
            print()
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
            return self  # Stay in the main menu
