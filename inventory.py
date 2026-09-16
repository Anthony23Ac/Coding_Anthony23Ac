from __future__ import annotations
from menu import MainMenu
from data import cache
import time 

def main_inventory(menu: MainMenu, inventory: Inventory):
    choice = 1

    while choice > 0 and choice < 7:
        menu.print_menu_inventory()
        choice = menu.get_input("Select a option", int, code=":")

        if not choice > 0 and not choice < 7: return

        if choice == 1:
            inventory.add_product(menu)
        elif choice == 2:
            inventory.remove_product(menu)

class product:

    def __init__(self, menu):
        self.name = ""
        self.type_of_product: str = ""
        self.colors: list = []
        self.sizes: list = []
        self.default_price = 0 
        self.stock_taking: dict = {}
        self.menu = menu

    # PROPERTIES 

    @property
    def default_price(self):
        return self._default_price

    @default_price.setter
    def default_price(self, default_price):
        if default_price >= 0:
            self._default_price = default_price
        else:
            self.audit_default_price(default_price,self.menu)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        check = False

        for idx, obj in enumerate(cache):
            if obj.name == name:
                check = True
                break

        if check:
            self.audit_name(name, self.menu)
        else:
            self._name = name

    # METHODS 

    def establish_product_inventory(self, menu: MainMenu):
        print("")
        print(f"{menu.set_color("] ==== · ", menu.secondary_color)}{menu.set_color("PRODUCT STOCK", menu.main_color)}{menu.set_color(" · ==== [", menu.secondary_color)}")
        print("")

        stock_taking = {}
        
        for idx, size in enumerate(self.sizes):
            print(menu.set_color(f"With the size {size}: ", menu.tertiary_color))
            stock_taking[size] = {}
            for i, color in enumerate(self.colors):
                stock_taking[size][color] = menu.get_input(f"How many stock do you have in {color} in {size}", int, code="?")

        self.stock_taking = stock_taking
        self.verify_and_add_cache()

        print("")
        print(menu.set_color("✓ Product stock added successfully.", menu.approved_color))
        time.sleep(1.3)

    def verify_and_add_cache(self):
        check = False
        index = 0 

        for idx, obj in enumerate(cache):
            if obj.name == self.name:
                check = True
                index = idx
                break
        
        if not check: 
            cache.append(self)
        else:
            cache[index] = self

    def audit_name(self, name, menu:MainMenu):

        print(menu.set_color("|", menu.tertiary_question_color))
        decision = menu.get_input(f"What would you like to write about {name} (Yes/No)", str, color=menu.tertiary_color, code="?")

        if decision.replace(" ","").lower() == "yes":
            self._name = name
            self.verify_and_add_cache()
            print(menu.set_color("|", menu.tertiary_question_color))
            print("")
            print(menu.set_color(f"Obj:{name} was eliminated properly. ", menu.error_color))
            print("")
            time.sleep(1.3)
        else:
            print(menu.set_color("|", menu.tertiary_question_color))
            self._name = menu.get_input(f"What another name would you like to give it", str, optional=name, code="?")


    def audit_default_price(self, default_price, menu:MainMenu):

        print("")
        print(menu.set_color("You can't put negative numbers in the default price. ", menu.error_color))
        print("")

        while True:
            price = menu.get_input(f"What does this cost for default in positive, no negative", int, color=menu.tertiary_color, code="?")
            if price >= 0:
                self._default_price = price
                break


        
class Inventory:

    def __init__(self, menu: MainMenu) -> None:
        pass

    def add_product(self, menu:MainMenu):
        print("")
        print(f"{menu.set_color("==========", menu.secondary_color)}{menu.set_color(" ADD GAME ", menu.main_color)}{menu.set_color("==========", menu.secondary_color)}")
        print("")

        obj = product(menu)

        print(menu.set_color("· DEFAULT SETTINGS ·", menu.secondary_color))
        print("")
        obj.name = menu.get_input("What name would you like to give it", str, code="?")
        print(menu.set_color("|", menu.tertiary_question_color))
        obj.type_of_product = menu.get_input("What type of product", str, code="?")
        print(menu.set_color("|", menu.tertiary_question_color))
        obj.colors = self.sort_inputs(menu.get_input("What colors does this come in (Separate with ,)", str, code="?"))
        print(menu.set_color("|", menu.tertiary_question_color))
        obj.sizes = self.sort_inputs(menu.get_input("What sizes does this come in? (Separate with ,)", str, code="?"))
        print(menu.set_color("|", menu.tertiary_question_color))
        obj.default_price = menu.get_input("What does this cost for default ($)", int, code="?")

        print("")
        default_price = menu.get_input("Would you like to create a product inventory (Yes/No)", str, color= menu.tertiary_color, code="?")

        if default_price.replace(" ", "").lower() == "no": 
            obj.verify_and_add_cache() 
            return
       
        obj.establish_product_inventory(menu)

    def remove_product(self, menu:MainMenu):
        print("")
        print(f"{menu.set_color("==========", menu.secondary_color)}{menu.set_color(" REMOVE PRODUCT ", menu.main_color)}{menu.set_color("==========", menu.secondary_color)}")
        print("")

    def display_list_products(self, menu:MainMenu):
        if cache:
            tidy_list = []
            spaces_column = 20

            for idx, product in enumerate(cache):
                tidy_list.append(f"{menu.set_color(f"{idx + 1}. ", menu.tertiary_color)}{menu.set_color(product, menu.quaternary_color)}")

            for idx, string in enumerate(tidy_list):
                if idx <= 9:
                    if len(string) <= 20:
                        print(string)
                    else:
                        ...
                    


    def sort_inputs(self, chain: str) -> list:
        return chain.replace(" ","").replace(".", "").lower().split(",")
