# 2. Descriptor: Validated Attribute

#     Create a descriptor PositiveInteger that only accepts positive integers.


class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{self.name} must be a positive integer")
        instance.__dict__[self.name] = value


class Descriptor:
    price = PositiveInteger()
    quantity = PositiveInteger()


# Testing the implementation
p = Descriptor()

# Valid assignments
p.price = 10
p.quantity = 5
print(f"Price: {p.price}, Quantity: {p.quantity}")

try:
    p.price = -5  # Raises ValueError
except ValueError as e:
    print(e)  # Output: "price must be a positive integer"


"""
Here's the step-by-step flow of the code execution for the descriptor-based attribute validation:
1. Class Definition Phase

    PositiveInteger descriptor class is defined:

        __set_name__, __get__, and __set__ methods are created

    Descriptor class is defined:

        Class attributes price and quantity are assigned PositiveInteger() instances

2. Descriptor Initialization

    When Descriptor class is created:

        Python calls __set_name__ for each descriptor instance:

            For price: PositiveInteger().__set_name__(Descriptor, 'price')

            For quantity: PositiveInteger().__set_name__(Descriptor, 'quantity')

        This stores the attribute names ('price', 'quantity') in each descriptor instance

3. Instance Creation and Usage

    p = Descriptor():

        Creates an instance of Descriptor

        The instance has its own __dict__ (currently empty)

    p.price = 10:

        Python sees price is a descriptor, so it calls:
        PositiveInteger().__set__(p, 10)

        Inside __set__:
        a. Checks isinstance(10, int) and 10 >= 0 → True
        b. Stores value in instance's __dict__: p.__dict__['price'] = 10

    p.quantity = 5:

        Same flow as above:
        PositiveInteger().__set__(p, 5)
        → Stores p.__dict__['quantity'] = 5

    print(f"Price: {p.price}, Quantity: {p.quantity}"):

        For p.price:
        a. Python sees price is a descriptor
        b. Calls PositiveInteger().__get__(p, Descriptor)
        c. Returns p.__dict__.get('price') → 10

        Same for p.quantity → returns 5

        Output: Price: 10, Quantity: 5

    p.price = -5:

        Calls PositiveInteger().__set__(p, -5)

        Inside __set__:
        a. Checks isinstance(-5, int) and -5 >= 0 → False
        b. Raises ValueError("price must be a positive integer")

4. Error Handling

    The try/except block catches the ValueError

    Prints the error message: price must be a positive integer

Key Points in the Flow:

    Descriptor Protocol Triggers:

        Attribute access → __get__

        Attribute assignment → __set__

    Storage:

        Values are stored in the instance's __dict__

        Descriptors mediate access to this storage

    Validation:

        Only happens during assignment (__set__)

        Reading (__get__) simply returns the stored value

    Class vs Instance:

        Descriptors are class attributes

        Values are stored per-instance in __dict__

This flow shows how descriptors provide controlled attribute access with validation while maintaining a clean interface (obj.attr = value).
New chat

"""
