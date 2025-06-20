# coffee_vending_machine.py
import threading
from typing import Dict
from concurrent.futures import ThreadPoolExecutor


class Ingredient:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity
        self.lock = threading.Lock()

    def update_quantity(self, amount: int):
        with self.lock:
            self.quantity += amount

    def consume(self, amount: int) -> bool:
        with self.lock:
            if self.quantity >= amount:
                self.quantity -= amount
                return True
            return False


class Coffee:
    def __init__(self, name: str, price: float, recipe: Dict[str, int]):
        self.name = name
        self.price = price
        self.recipe = recipe


class Payment:
    def __init__(self, amount: float):
        self.amount = amount


class CoffeeMachine:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(CoffeeMachine, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return

        self.ingredients: Dict[str, Ingredient] = {
            "water": Ingredient("water", 5000),
            "milk": Ingredient("milk", 3000),
            "coffee_beans": Ingredient("coffee_beans", 1000),
        }

        self.menu: Dict[str, Coffee] = {
            "espresso": Coffee("espresso", 2.5, {"water": 50, "coffee_beans": 18}),
            "cappuccino": Coffee(
                "cappuccino", 3.0, {"water": 50, "milk": 60, "coffee_beans": 18}
            ),
            "latte": Coffee(
                "latte", 3.5, {"water": 30, "milk": 120, "coffee_beans": 18}
            ),
        }

        self._initialized = True

    def display_menu(self):
        print("Available Coffee Options:")
        for name, coffee in self.menu.items():
            print(f"{name.title()}: ${coffee.price}")

    def has_enough_ingredients(self, coffee: Coffee) -> bool:
        return all(
            self.ingredients[ing].quantity >= amt for ing, amt in coffee.recipe.items()
        )

    def update_ingredients(self, coffee: Coffee):
        for ing, amt in coffee.recipe.items():
            if not self.ingredients[ing].consume(amt):
                raise ValueError(f"Not enough {ing}")

    def make_coffee(self, coffee_name: str, payment: Payment):
        if coffee_name not in self.menu:
            print("Invalid coffee selection.")
            return

        coffee = self.menu[coffee_name]

        if payment.amount < coffee.price:
            print("Insufficient payment.")
            return

        if not self.has_enough_ingredients(coffee):
            print("Not enough ingredients to make the coffee.")
            return

        self.update_ingredients(coffee)
        change = round(payment.amount - coffee.price, 2)
        print(f"Dispensing {coffee.name}. Change returned: ${change}")

    def check_inventory(self):
        print("Ingredient Inventory:")
        for name, ing in self.ingredients.items():
            print(f"{name}: {ing.quantity}")

        for ing in self.ingredients.values():
            if ing.quantity < 100:
                print(f"Warning: {ing.name} running low!")


class CoffeeVendingMachine:
    def __init__(self):
        self.machine = CoffeeMachine()

    def run(self):
        self.machine.display_menu()

        def user_request(coffee_name: str, payment_amt: float):
            payment = Payment(payment_amt)
            self.machine.make_coffee(coffee_name, payment)

        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.submit(user_request, "espresso", 3.0)
            executor.submit(user_request, "latte", 4.0)
            executor.submit(user_request, "cappuccino", 3.0)

        self.machine.check_inventory()


if __name__ == "__main__":
    app = CoffeeVendingMachine()
    app.run()
