from data import option_main_menu
from data import option_inventory

class MainMenu:
    """
    This object is for having all the functions, attributes and properties to have very tied.
    """

    def __init__(self, main_color, secondary_color, tertiary_color, quaternary_color, approved_color, error_color, main_question_color, secondary_question_color, tertiary_question_color):
        if not isinstance(main_color, int) or not isinstance(secondary_color, int) or not isinstance(tertiary_color, int) or not isinstance(quaternary_color, int):
            raise ValueError("Ups! There was an error creating the object: There is a value that is another value type")

        # Color Palette
        self.main_color = main_color
        self.secondary_color = secondary_color
        self.tertiary_color = tertiary_color
        self.quaternary_color = quaternary_color

        # Special Colors

        self.approved_color = approved_color
        self.error_color = error_color
        self.main_question_color = main_question_color
        self.secondary_question_color = secondary_question_color
        self.tertiary_question_color = tertiary_question_color

    def set_color(self, text: str, color: int) -> str:
        """Apply an ANSI color code to the given text and return the formatted string."""
        return f"\033[{color}m{text}\033[0m"

    def get_input(self, text: str, type_value: type, color = 95, optional="", code="", obj_menu="", menu=object):
        """
        Get the user's input to create a interactive program

        parameters:

        - Text: the string that the programer gives to print and ask in the input.
        - Type_Value: the value type that has to be in the input.
        - Color: The color that'll be in the text of input.
        - optional: Is a string that is not to be the same with the user's input with the string gaves by the programer.
        - code: Is a code that is to divide multiples functions.
        - Obj_menu: Is a code that is to know what menu has to print.
        - menu: is the object menu

        """

        def question_fragment():
            return type_value(input(f"{self.set_color("·", self.secondary_question_color)} {self.set_color(text, color)}{self.set_color("?", self.tertiary_question_color)}{self.set_color(":", self.secondary_question_color)} "))
        
        while True: 
            choice = type_value 

            try:
                if code == "?":
                    choice = question_fragment()
                elif code == "Y/N":
                    choice = question_fragment().replace(" ", "").lower()

                    if choice != "no" and choice != "yes":
                        print("")
                        print(self.set_color(f"Ups! It can only be (Yes/Not) instead of {choice}. ", self.error_color))
                        print("")
                        continue

                    return choice
                elif code == ":":

                    if obj_menu == "main_menu":
                        menu.print_main_menu()
                    elif obj_menu == "main_inventory":
                        menu.print_menu_inventory()
                    
                    choice = type_value(input(f"{self.set_color(text, color)}{self.set_color(":", self.secondary_question_color)} "))
                else:
                    choice = type_value(input(self.set_color(text, color)))

                if optional != "":
                    if str(choice).replace(" ", "").lower() == str(optional).replace(" ","").lower():
                        print("")
                        print(self.set_color(f"Ups! It can't be another the same value. ", self.error_color))
                        print("")
                        continue

            except Exception as error: 
                print("")
                print(self.set_color(f"Ups! There was an error: {error}", 91))
                print("")
            else:
                return choice

    def print_main_menu(self):
        print("")
        print(self.set_color("================================", self.secondary_color))
        print(self.set_color("           MAIN MENU", self.main_color))
        print(self.set_color("================================", self.secondary_color))

        for idx, value in enumerate(option_main_menu):
            print(f"{self.set_color(f"{idx + 1}.", self.tertiary_color)} {self.set_color(value, self.quaternary_color)}")

        print(self.set_color("================================", self.secondary_color))

    def print_menu_inventory(self):
        print("")
        print(self.set_color("================================", self.secondary_color))
        print(self.set_color("       INVENTORY MANAGER", self.main_color))
        print(self.set_color("================================", self.secondary_color))

        for idx, value in enumerate(option_inventory):
            print(f"{self.set_color(f"{idx + 1}.", self.tertiary_color)} {self.set_color(value, self.quaternary_color)}")

        print(self.set_color("================================", self.secondary_color))


    def leave_program(self):
        print(self.set_color("Thank you for visiting our program! ", self.quaternary_color))
        print("")




