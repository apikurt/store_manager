from .base import MenuBase


class LoginMenu(MenuBase):
    def __init__(self, data_manager):
        super().__init__(data_manager)

    def run(self):
        self.clear_screen()
        print("--- Staff Login Menu ---")

        print("Please enter your login credentials.")
        print()
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        staff_member = self.data_manager.login_staff(username, password)
        if staff_member:
            self.data_manager.current_staff = staff_member
            print(f"Welcome, {staff_member.username}!")
            input("Press Enter to continue...")
            from .main_menu import MainMenu

            return MainMenu(self.data_manager)  # Proceed to main menu
        else:
            print("Invalid Username or Password. Please try again.")
            input("Press Enter to try again...")
            return self  # Stay in the login menu
