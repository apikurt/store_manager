from .base import MenuBase


class LoginMenu(MenuBase):
    def run(self):
        self.show_header("Staff Login")

        print("Please enter your login credentials.")
        print()
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        staff_member = self.data_manager.login_staff(username, password)
        if staff_member:
            self.data_manager.current_staff = staff_member
            print()
            print(f"Welcome, {staff_member.username}!")
            input("Press Enter to continue...")
            from .main_menu import MainMenu

            return MainMenu(self.data_manager)  # Proceed to main menu
        else:
            print()
            print("Invalid username or password.")
            print()
            print("Options:")
            print("1. Try Again")
            print("2. Exit Application")
            print()
            choice = input("Select an option: ").strip()
            if choice == "1":
                return self  # Retry login
            elif choice == "2":
                self.exit_application()
            else:
                print("Invalid choice.")
                input("Press Enter to try again...")
                return self
