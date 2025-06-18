import threading
from datetime import datetime
import uuid


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_available(self):
        return self.quantity > 0

    def reduce_stock(self, count: int = 1):
        if self.quantity >= count:
            self.quantity -= count
        else:
            raise Exception("Insufficient product stock")


class Money:
    def __init__(self):
        self.denominations = {
            0.5: 10,
            1: 10,
            5: 10,
            10: 10,
            20: 5,
            50: 5,
            100: 2,
        }  # example

    def add(self, denomination, count=1):
        self.denominations[denomination] = (
            self.denominations.get(denomination, 0) + count
        )

    def remove(self, denomination, count=1):
        if self.denominations.get(denomination, 0) >= count:
            self.denominations[denomination] -= count
        else:
            raise Exception("Insufficient denomination")

    def get_total(self):
        return sum(den * count for den, count in self.denominations.items())

    def get_change(self, amount):
        # Greedy change return
        result = {}
        for denom in sorted(self.denominations.keys(), reverse=True):
            while denom <= amount and self.denominations[denom] > 0:
                amount -= denom
                amount = round(amount, 2)  # Avoid floating-point issues
                result[denom] = result.get(denom, 0) + 1
                self.remove(denom)
        if amount > 0:
            raise Exception("Unable to return exact change")
        return result


class Slot:
    def __init__(self, product: Product):
        self.product = product

    def dispense(self):
        self.product.reduce_stock()


class Transaction:
    def __init__(self, slot: Slot, inserted_amount: float):
        self.timestamp = datetime.now()
        self.slot = slot
        self.inserted_amount = inserted_amount
        self.change = {}

    def is_sufficient_fund(self):
        return self.inserted_amount >= self.slot.product.price


class VendingMachine:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.slots = {}
                    cls._instance.cash = Money()
        return cls._instance

    def add_slot(self, product: Product):
        self.slots[product.id] = Slot(product)

    def restock(self, product_id, count):
        self.slots[product_id].product.quantity += count

    def insert_money(self, money_list):  # money_list = [(denomination, count)]
        total = 0
        for denom, cnt in money_list:
            total += denom * cnt
            self.cash.add(denom, cnt)
        return total

    def buy_product(self, product_id, inserted_money):
        if product_id not in self.slots:
            raise Exception("Invalid product")

        slot = self.slots[product_id]
        transaction = Transaction(slot, inserted_money)

        if not slot.product.is_available():
            raise Exception("Product out of stock")

        if not transaction.is_sufficient_fund():
            raise Exception("Insufficient funds")

        # Dispense product
        slot.dispense()

        # Return change
        change_needed = round(inserted_money - slot.product.price, 2)
        change = self.cash.get_change(change_needed)

        transaction.change = change
        return f"Dispensed: {slot.product.name}, Change: {change}"


# -------------------------------------------------------------------------------


"""


import uuid
import threading
from datetime import datetime


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.lock = threading.Lock()  # For stock-level concurrency

    def is_available(self):
        return self.quantity > 0

    def reduce_stock(self, count: int = 1):
        with self.lock:
            if self.quantity >= count:
                self.quantity -= count
            else:
                raise Exception("Insufficient product stock")


class Money:
    def __init__(self):
        self.denominations = {0.5: 10, 1: 10, 5: 10, 10: 10, 20: 5, 50: 5, 100: 2}
        self.lock = threading.Lock()

    def add(self, denomination, count=1):
        with self.lock:
            self.denominations[denomination] = self.denominations.get(denomination, 0) + count

    def remove(self, denomination, count=1):
        if self.denominations.get(denomination, 0) >= count:
            self.denominations[denomination] -= count
        else:
            raise Exception(f"Insufficient denomination for {denomination}")

    def get_total(self):
        return sum(den * count for den, count in self.denominations.items())

    def get_change(self, amount):
        with self.lock:
            change = {}
            for denom in sorted(self.denominations.keys(), reverse=True):
                while denom <= amount and self.denominations[denom] > 0:
                    amount -= denom
                    amount = round(amount, 2)
                    change[denom] = change.get(denom, 0) + 1
                    self.remove(denom)
                if amount == 0:
                    break
            if amount != 0:
                raise Exception("Unable to provide exact change")
            return change


class Slot:
    def __init__(self, product: Product):
        self.product = product

    def dispense(self):
        self.product.reduce_stock()


class Transaction:
    def __init__(self, slot: Slot, inserted_amount: float):
        self.timestamp = datetime.now()
        self.slot = slot
        self.inserted_amount = inserted_amount
        self.change = {}

    def is_sufficient_fund(self):
        return self.inserted_amount >= self.slot.product.price


class VendingMachine:
    _instance = None
    _singleton_lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._singleton_lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.slots = {}
                    cls._instance.cash = Money()
                    cls._instance.lock = threading.Lock()  # Transaction-level lock
        return cls._instance

    def add_slot(self, product: Product):
        self.slots[product.id] = Slot(product)

    def restock(self, product_id, count):
        if product_id in self.slots:
            self.slots[product_id].product.quantity += count
        else:
            raise Exception("Invalid product ID")

    def insert_money(self, money_list):  # money_list = [(denomination, count)]
        total = 0
        for denom, cnt in money_list:
            total += denom * cnt
            self.cash.add(denom, cnt)
        return total

    def buy_product(self, product_id, inserted_money):
        with self.lock:
            if product_id not in self.slots:
                raise Exception("Invalid product")

            slot = self.slots[product_id]
            product = slot.product

            if not product.is_available():
                raise Exception("Product out of stock")

            if inserted_money < product.price:
                raise Exception("Insufficient funds")

            # Dispense product
            product.reduce_stock()

            # Return change
            change_needed = round(inserted_money - product.price, 2)
            change = self.cash.get_change(change_needed)

            return f"Dispensed: {product.name}, Change: {change}"


import threading

def simulate_user(vm, product_id, inserted_amount):
    try:
        result = vm.buy_product(product_id, inserted_amount)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# Setup
vm = VendingMachine()
product = Product("Coke", 10.0, 2)
vm.add_slot(product)
vm.insert_money([(10, 5)])

# Simulate 5 users trying to buy 2 available Cokes
threads = [threading.Thread(target=simulate_user, args=(vm, product.id, 10.0)) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()




"""
