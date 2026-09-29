
# Import All Modules
from menu import MainMenu
from inventory import main_inventory, Inventory

def main():
    choice = 1 
    menu = MainMenu(96,34,33,35,92,91,95,96, 97)
    inventory = Inventory(menu)

    while choice > 0 and choice < 4:

        choice = menu.get_input("Select an option", int, code=":", obj_menu= "main_menu", menu=menu)
        print("")

        if choice == 1:
            main_inventory(menu, inventory)

    menu.leave_program()
        

if __name__ == "__main__":
    main()
