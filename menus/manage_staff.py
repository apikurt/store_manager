from staff import Manager, Worker

from .base import MenuBase


class ManageStaffMenu(MenuBase):
    def run(self):
        from .main_menu import MainMenu

        self.show_header("Manage Staff")
        self.show_user()

        if self.data_manager.current_staff.role != "manager":
            print("Only managers can manage staff accounts.")
            input("Press Enter to return to the Main Menu...")
            return MainMenu(self.data_manager)

        print("Options:")
        print("1. Create Staff Account")
        print("2. List Staff")
        print("3. Return to Main Menu")
        print()
        choice = input("Select an option: ").strip()
        if choice == "1":
            return self._create_staff()
        if choice == "2":
            return self._list_staff()
        if choice == "3":
            return MainMenu(self.data_manager)
        print()
        print("Invalid choice.")
        input("Press Enter to return to the Main Menu...")
        return MainMenu(self.data_manager)

    def _create_staff(self):
        from .main_menu import MainMenu

        self.show_header("Create Staff Account")
        self.show_user()

        existing_staff = self.data_manager.load_data().get("staff", [])
        existing_usernames = {s.username.lower() for s in existing_staff}

        username = input("Username: ").strip()
        if not username:
            print()
            print("Username cannot be empty.")
            input("Press Enter to return to the Main Menu...")
            return MainMenu(self.data_manager)
        if username.lower() in existing_usernames:
            print()
            print("That username already exists.")
            input("Press Enter to return to the Main Menu...")
            return MainMenu(self.data_manager)

        print()
        print("Role:")
        print("1. Worker (default)")
        print("2. Manager")
        role_choice = input("Select an option: ").strip()
        password = input("Password: ").strip()
        if not password:
            print()
            print("Password cannot be empty.")
            input("Press Enter to return to the Main Menu...")
            return MainMenu(self.data_manager)

        employee_id = self._next_employee_id(existing_staff)
        if role_choice == "2":
            new_staff = Manager(
                username=username,
                employee_id=employee_id,
                password=password,
            )
        else:
            new_staff = Worker(
                username=username,
                employee_id=employee_id,
                password=password,
            )

        self.data_manager.add_new_staff(new_staff)
        print()
        print(f"Staff account created for '{username}' ({new_staff.role}).")
        input("Press Enter to return to the Main Menu...")
        return MainMenu(self.data_manager)

    def _list_staff(self):
        from .main_menu import MainMenu

        self.show_header("Staff List")
        self.show_user()

        staff_list = self.data_manager.load_data().get("staff", [])
        if not staff_list:
            print("No staff accounts found.")
        else:
            print("Staff:")
            print()
            print(f"{'Username':<20} {'Employee ID':<12} {'Role':<10}")
            print("-" * 46)
            for staff in staff_list:
                print(f"{staff.username:<20} {staff.employee_id:<12} {staff.role:<10}")
        print()
        input("Press Enter to return to the Main Menu...")
        return MainMenu(self.data_manager)

    def _next_employee_id(self, staff_list) -> str:
        max_id = 0
        for staff in staff_list:
            raw_id = staff.employee_id.strip()
            if raw_id.upper().startswith("EMP"):
                raw_id = raw_id[3:]
            try:
                max_id = max(max_id, int(raw_id))
            except ValueError:
                continue
        return f"EMP{max_id + 1:03d}"
