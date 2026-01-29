from .base import MenuBase


class AddProductMenu(MenuBase):
    def __init__(self, data_manager):
        super().__init__(data_manager)

    def run(self):
        from .manage_inventory import ManageInventoryMenu

        self.clear_screen()

        print(f"Logged in as: {self.data_manager.current_staff.username}")
        print()

        print("--- Add Product Menu ---")
        name = input("Enter product name: ").strip()
        price = input("Enter product price: ").strip()
        stock = input("Enter initial stock quantity: ").strip()

        print("\nSelect product category:")
        print("1. Electronics")
        print("2. Clothing")
        print("3. Cleaning Supplies")
        category_choice = input(
            "Enter the number corresponding to the category: "
        ).strip()
        if category_choice == "1":
            category = "Electronics"
            warranty_period = input("Enter warranty period (in months): ").strip()
            product = self.data_manager.product_from_dict(
                {
                    "name": name,
                    "price": price,
                    "stock": stock,
                    "category": category,
                    "warranty_months": warranty_period,
                }
            )
            self.data_manager.add_new_product(product)

        elif category_choice == "2":
            category = "Clothing"
            size = input("Enter size (e.g., S, M, L, XL): ").strip()
            material = input("Enter material (e.g., Cotton, Polyester): ").strip()
            product = self.data_manager.product_from_dict(
                {
                    "name": name,
                    "price": price,
                    "stock": stock,
                    "category": category,
                    "size": size,
                    "material": material,
                }
            )
            self.data_manager.add_new_product(product)

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
            product = self.data_manager.product_from_dict(
                {
                    "name": name,
                    "price": price,
                    "stock": stock,
                    "category": category,
                    "material_state": material_state,
                }
            )
            self.data_manager.add_new_product(product)
        else:
            print("Invalid category choice. Returning to Inventory Management Menu.")
            input("Press Enter to continue...")

            return ManageInventoryMenu(self.data_manager)

        print(f"Product '{name}' added successfully!")
        input("Press Enter to return to Inventory Management Menu...")

        return ManageInventoryMenu(
            self.data_manager
        )  # Return to Inventory Management Menu
