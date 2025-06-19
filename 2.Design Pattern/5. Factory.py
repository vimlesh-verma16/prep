from abc import ABC, abstractmethod


# Step 1: Base Interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


# Step 2: Concrete Implementations
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"📧 Email sent: {message}")


class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"📱 SMS sent: {message}")


class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"📲 Push Notification sent: {message}")


# Step 3: Factory Function
def notification_factory(type_: str) -> Notification:
    match type_.lower():
        case "email":
            return EmailNotification()
        case "sms":
            return SMSNotification()
        case "push":
            return PushNotification()
        case _:
            raise ValueError(f"Unsupported notification type: {type_}")


# Step 4: Client Code
if __name__ == "__main__":
    type_input = input("Enter notification type (email/sms/push): ")
    notification = notification_factory(type_input)
    notification.send("Hello from modern Python Factory Pattern!")

"""
✅ Why Use It?

Because:

    You want to decouple object creation from usage.

    You have many related classes, and the client should not care which one is created.

    You want to encapsulate object creation logic in one place.
    
    
✅ When to Use It

Use Factory Pattern when:

    You need to create objects based on dynamic input (user input, config file, etc.).

    Object creation involves complex logic or conditional branching.

    You want to adhere to Open/Closed Principle – easily add new object types without changing client code.

    You want to avoid code like:

if type == "A":
    obj = A()
elif type == "B":
    obj = B()

in multiple places across your code.

"""


# Combination of strategy with factory
"""
from abc import ABC, abstractmethod

# Step 1: Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Step 2: Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"💳 Paid ₹{amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"💻 Paid ₹{amount} using PayPal")

class UpiPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"📱 Paid ₹{amount} using UPI")

# Step 3: Factory to create strategy
def payment_strategy_factory(method: str) -> PaymentStrategy:
    match method.lower():
        case "credit":
            return CreditCardPayment()
        case "paypal":
            return PayPalPayment()
        case "upi":
            return UpiPayment()
        case _:
            raise ValueError("Unknown payment method")

# Step 4: Context Class (uses Strategy)
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount: float) -> None:
        self.strategy.pay(amount)

# Step 5: Client Code
if __name__ == "__main__":
    method = input("Enter payment method (credit/paypal/upi): ")
    amount = float(input("Enter amount to pay: "))

    strategy = payment_strategy_factory(method)
    processor = PaymentProcessor(strategy)
    processor.process_payment(amount)

"""
