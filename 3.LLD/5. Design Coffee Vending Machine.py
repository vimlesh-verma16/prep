# Flow: show_menu ->   select coffee -> check_for_inventory -> available -> insert_amount -> dispense_coffer ->dispense_change -> show_menu

from enum import Enum
from abc import ABC, abstractmethod


class CoffeeType(Enum):
    BLACK_COFFEE = "black_coffee"
    LATTE = "latte"
    AMERICANO = "americano"
    ESPRESSO = "espresso"


class CoffeeMaker(ABC):
    @abstractmethod
    def make_coffee(self):
        pass


class BlackCoffeeMaker(CoffeeMaker):
    def make_coffee(self):
        print("make coffe")


class LatteMaker(CoffeeMaker):
    def make_coffee(self):
        print("make coffe")


class AmericanoMaker(CoffeeMaker):
    def make_coffee(self):
        print("make coffe")


class EspressoMaker(CoffeeMaker):
    def make_coffee(self):
        print("make coffe")


class SelectCoffeMaker:

    def make_coffe(self, strategy):
        strategy.make_coffee()


class FUND:
    def __init__(self):
        self.denomination = {10: 10, 20: 2, 50: 1}

    def check_funds(self, coffe):
        return True


class Coffee:
    def __init__(self, coffee_type, price):
        self.price = price
        self.coffee_type = coffee_type


class Machine:
    def __init__(self):
        self.inventory = {
            "black_coffee": 5,
            "latte": 10,
            "americano": 15,
            "espresso": 10,
        }
        self.price = {"black_coffee": 5, "latte": 10, "americano": 15, "espresso": 10}
        self.funds = FUND()
        self.c_make = SelectCoffeMaker()

    def show_menu(self):
        for co in CoffeeType:
            print(co.name, co.value)

    def select_coffee(self, selection, coffe_maker_obj):
        coffe = Coffee(selection, self.price[selection])
        if selection in self.inventory and self.funds.check_funds(coffe):
            self.c_make.make_coffe(coffe_maker_obj)
            self.dispense()

    @staticmethod
    def dispense():
        print("Please collect coffee and change")

    def latte(self):
        self.select_coffee(CoffeeType.LATTE.value, LatteMaker())

    def espresso(self):
        self.select_coffee(CoffeeType.ESPRESSO.value, EspressoMaker())


class DEMO:
    @staticmethod
    def run():
        CM = Machine()
        CM.show_menu()
        CM.latte()
        CM.espresso()
        CM.show_menu


if __name__ == "__main__":
    DEMO.run()
