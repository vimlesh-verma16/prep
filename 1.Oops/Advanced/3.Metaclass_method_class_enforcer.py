# 3. Metaclass: Method Name Enforcer
# Create a metaclass MethodNameValidator that ensures all method names in a class must be lowercase (e.g., no MyMethod() allowed).


class MethodValidator(type):
    def __new__(cls, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            print(attr_name, attr_value)
            if not attr_name.islower():
                raise ValueError("Method name should be lower case")
        return super().__new__(cls, name, bases, namespace)


class Myclass(metaclass=MethodValidator):
    def My_Method(self):
        print("My_Method")

    def UpperCase_Method(self):
        print("UpperCase_Method")


m = Myclass()


"""
Why Use This Metaclass?

    API Consistency: Ensures uniform method naming across large codebases

    Style Enforcement: Automates PEP 8 naming convention checks

    Early Validation: Catches naming issues at class definition time

    Framework Development: Useful for creating opinionated frameworks
"""
