menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}


def show_menu(menu_dict):
    if len(menu_dict) == 0:
        print("The menu is empty.")
    else:
        print("Current menu:")
        for drink in menu_dict:
            print(f"{drink} - {menu_dict[drink]:.1f}₪")


def add_item(menu_dict):
    drink_name = input("Enter new drink name: ")

    if drink_name in menu_dict:
        print("Item already exists!")
    else:
        price = float(input("Enter price: "))
        menu_dict[drink_name] = price
        print(f'"{drink_name}" added!')


def update_price(menu_dict):
    drink_name = input("Which drink do you want to update? ")

    if drink_name in menu_dict:
        new_price = float(input("Enter the new price: "))
        menu_dict[drink_name] = new_price
        print("Price updated!")
    else:
        print("Item not found.")


def delete_item(menu_dict):
    drink_name = input("Which drink do you want to delete? ")

    if drink_name in menu_dict:
        del menu_dict[drink_name]
        print("Item deleted.")
    else:
        print("Item not found.")


def show_options():
    print("What would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")


def run_coffee_shop():
    while True:
        show_options()
        choice = input("> ")

        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            update_price(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


run_coffee_shop()
