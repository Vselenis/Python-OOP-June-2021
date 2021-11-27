from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if food_type == "Bread":
            new_br = Bread(name, price)
            if new_br in self.food_menu:
                raise Exception(f"{food_type} {name} is already in the menu!")
            else:
                return f"Added {name} ({food_type}) to the food menu"
        elif food_type == "Cake":
            new_br = Cake(name, price)
            if new_br in self.food_menu:
                raise Exception(f"{food_type} {name} is already in the menu!")
            else:
                return f"Added {name} ({food_type}) to the food menu"


    def add_drink(self, drink_type, name, portion, brand):
        if drink_type == "Tea":
            new_dr = Tea(name, portion, brand)
            if new_dr in self.drinks_menu:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            else:
                return f"Added {name} ({brand}) to the drink menu"

        elif drink_type == "Water":
            new_dr = Water(name, portion, brand)
            if new_dr in self.drinks_menu:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            else:
                return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
            if new_table in self.tables_repository:
                raise Exception(f"Table {table_number} is already in the bakery!")
            else:
                return f"Added table number {table_number} in the bakery"

        elif table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)
            if new_table in self.tables_repository:
                raise Exception(f"Table {table_number} is already in the bakery!")
            else:
                return f"Added table number {table_number} in the bakery"


    def reserve_table(self, number_of_people):
        rs = [r for r in self.tables_repository if r.capacity >= number_of_people]
        for el in rs:
            if el.is_reserved == False:
                return f"Table {el.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"



    def order_food(self, table_number, *food_name):
        # food_name = list(food_name)
        # find_table = [t for t in self.tables_repository if t.table_number == table_number]
        # if len(find_table) == 0:
        #     return f"Could not find table {table_number}"
        # else:
        #     positive_result = ""
        #     negative_result = ""
        #     negative_result += f"{self.name} does not have in the menu:\n"
        #     positive_result += f"Table {table_number} ordered:\n"
        #     for drink in drinks_name:
        #         if drink in self.drinks_menu:
        #             positive_result += f"{drink.name} {drink.brand} - {drink.portion}ml - {drink.price}lv\n"
        #         else:
        #             negative_result += f"{drink.name}\n"
        #
        #     return positive_result + negative_result

    def order_drink(self, table_number, *drinks_name):
        drinks_name = list(drinks_name)
        find_table = [t for t in self.tables_repository if t.table_number == table_number]
        if len(find_table) == 0:
            return f"Could not find table {table_number}"
        else:
            positive_result = ""
            negative_result = ""
            negative_result += f"{self.name} does not have in the menu:\n"
            positive_result += f"Table {table_number} ordered:\n"
            for drink in drinks_name:
                if drink in self.drinks_menu:
                    positive_result += f"{drink.name} {drink.brand} - {drink.portion}ml - {drink.price}lv\n"
                else:
                    negative_result += f"{drink.name}\n"

            return positive_result + negative_result


    def leave_table(self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass