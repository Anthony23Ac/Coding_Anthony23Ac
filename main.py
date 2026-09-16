# Import All Modules
from menu import MainMenu
from inventory import main_inventory, Inventory

def main():
    choice = 1 
    menu = MainMenu(96,34,33,35,92,91,95,96, 97)
    inventory = Inventory(menu)

    while choice > 0 and choice < 4:

        menu.print_main_menu()
        choice = menu.get_input("Select a option", int, code=":")

        if not choice > 0 and not choice < 4: break
        print("")

        if choice == 1:
            main_inventory(menu, inventory)

    menu.leave_program()
        

if __name__ == "__main__":
    main()
