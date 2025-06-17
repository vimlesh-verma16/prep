# 1. Magic Methods: Vector Class
#     Implement a Vector class that supports:
#     +, -, and * operations (operator overloading)
#     __str__ and __repr__ for clean printing
#     == to compare vectors
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# print(v1 + v2)  # Vector(4, 6)
# print(v1 * 3)  # Vector(9, 12)
# print(v1 == v2)  # False


# class sign
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.a + other.a, self.b + other.b)
        raise ValueError("Other is not Vector type")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.a - other.a, self.b - other.b)
        raise ValueError("Other is not Vector type")

    def __mul__(self, scaler):
        if isinstance(scaler, (int, float)):
            return Vector(self.a * scaler, self.b * scaler)
        raise ValueError("Other is not float/int type")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.a == other.a and self.b == other.b
        return False

    def __str__(self):
        return f"Vector({self.a},{self.b})"

    def __repr__(self):
        return f"Vector({self.a},{self.b})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)
print(v1 - v2)
print(v2 * 3)
print(v1 == v2)
print(v1 == Vector(3, 4))
