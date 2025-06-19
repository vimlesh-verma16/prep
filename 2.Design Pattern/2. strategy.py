class PasswordGenerator:  # without strategy pattern
    def generate_password(self, password_type="alpha"):
        if password_type == "alpha":
            # Build string password whatever way you want to do it
            return "abcdefghigklmnopqrstuvwxyz"
        elif password_type == "numeric":
            # Generate random numeric password
            return "1234567890"
        else:
            # Default mix of character and numbers
            return "abcd1234"


if __name__ == "__main__":
    pg = PasswordGenerator()
    password = pg.generate_password(password_type="alpha")
    print("Generated password:--", password)

# --------------------------------------------------------------------------------------------------

"""  strategy pattern """


from abc import ABC, abstractmethod


# Strategy Interface
class PasswordStrategy(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass


# Concrete Strategies
class AlphaStrategy(PasswordStrategy):
    def generate(self) -> str:
        return "abcdefghigklmnopqrstuvwxyz"


class NumericStrategy(PasswordStrategy):
    def generate(self) -> str:
        return "1234567890"


class MixedStrategy(PasswordStrategy):
    def generate(self) -> str:
        return "abcd1234"


# Context that uses provided strategy
class PasswordGenerator:
    def generate_password(self, strategy: PasswordStrategy) -> str:
        return strategy.generate()


# Usage
if __name__ == "__main__":
    pg = PasswordGenerator()

    # You provide the strategy directly
    print("Alpha:", pg.generate_password(AlphaStrategy()))
    print("Numeric:", pg.generate_password(NumericStrategy()))
    print("Mixed:", pg.generate_password(MixedStrategy()))


# The Strategy Pattern is a behavioral design pattern that lets you:

# Define a family of algorithms (different ways to do something)
# Encapsulate each algorithm in its own class
# Make them interchangeable at runtime


# When to Use This Implementation

#     Multiple Algorithms: When you need different password generation methods (alpha/numeric/mixed)

#     Runtime Flexibility: When the algorithm needs to change dynamically during execution

#     Avoid Conditionals: When you want to replace complex if-else or switch-case logic

#     Testing: When you need to isolate and test different algorithms separately

#     Future Extensions: When new password types might be added later
