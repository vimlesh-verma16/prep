# Encapsulation

#     Create a BankAccount class with private attribute __balance. Add methods to deposit, withdraw, and get balance securely.


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited succesfully")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("insufficient balance")
        else:
            self.__balance -= amount
            print("Successfully withdrawn amount ")


BA = BankAccount()
BA.deposit(10)
BA.withdraw(2)
print(f"My balance is {BA.balance}")
