from .base import MenuBase


class AddProductMenu(MenuBase):
    def run(self):
        from .manage_inventory import ManageInventoryMenu

        self.show_header("Add Product")
        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        print("Product Details:")
        name = input("Enter product name: ").strip()
        price = input("Enter product price: ").strip()
        stock = input("Enter initial stock quantity: ").strip()

        print()
        print("Category:")
        print("1. Electronics")
        print("2. Clothing")
        print("3. Cleaning Supplies")
        category_choice = input("Select an option: ").strip()
        product_data = {"name": name, "price": price, "stock": stock}
        if category_choice == "1":
            category = "Electronics"
            warranty_period = input("Enter warranty period (in months): ").strip()
            product_data.update(
                {
                    "category": category,
                    "warranty_months": warranty_period,
                }
            )
        elif category_choice == "2":
            category = "Clothing"
            size = input("Enter size (e.g., S, M, L, XL): ").strip()
            material = input("Enter material (e.g., Cotton, Polyester): ").strip()
            product_data.update(
                {
                    "category": category,
                    "size": size,
                    "material": material,
                }
            )
        elif category_choice == "3":
            category = "Cleaning Supplies"
            print("Select material state:")
            print("1. Liquid")
            print("2. Solid")
            print("3. Gas")
            state_choice = input(
                "Enter the number corresponding to the material state: "
            ).strip()
            material_state = "liquid"  # Default
            if state_choice == "1":
                material_state = "liquid"
            elif state_choice == "2":
                material_state = "solid"
            elif state_choice == "3":
                material_state = "gas"
            else:
                print("Invalid material state choice. Defaulting to 'liquid'.")
            product_data.update(
                {
                    "category": category,
                    "material_state": material_state,
                }
            )
        else:
            print()
            print("Invalid category choice. Returning to Inventory Management Menu.")
            input("Press Enter to continue...")

            return ManageInventoryMenu(self.data_manager)

        product = self.data_manager.product_from_dict(product_data)
        if product is None:
            print()
            print("Invalid product details. Please try again.")
            input("Press Enter to continue...")
            return ManageInventoryMenu(self.data_manager)

        self.data_manager.add_new_product(product)

        print()
        print(f"Product '{name}' added successfully!")
        print()

        print("Options:")
        print("1. Add Another Product")
        print("2. Return to Inventory Management Menu")
        print("3. Return to Main Menu")
        print("4. Exit Application")
        print()

        choice = input("Select an option: ").strip()

        if choice == "1":  # Restart Add Product Menu
            return self
        elif choice == "2":  # Return to Inventory Management Menu
            return ManageInventoryMenu(self.data_manager)

        elif choice == "3":  # Return to Main Menu
            from .main_menu import MainMenu

            return MainMenu(self.data_manager)
        elif choice == "4":
            self.exit_application()
        else:
            print()
            print("Invalid choice. Returning to Inventory Management Menu.")
            input("Press Enter to continue...")
            return ManageInventoryMenu(
                self.data_manager
            )  # Return to Inventory Management Menu by default
