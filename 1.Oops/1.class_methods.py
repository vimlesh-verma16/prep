# @classmethod and @staticmethod

#     Create a Circle class with a class method from_diameter(d) to create a circle using diameter, and a static method is_valid_radius(r).


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, d):
        r = d // 2
        if cls.is_valid_radius(r):
            print(f"circle of radius {d//2} is made")
            return cls(r)
        else:
            print("cannot make a circle with given radius making default radius 1")
            return cls(1)

    @staticmethod
    def is_valid_radius(r):
        if r > 0:
            return True
        return False


c1 = Circle.from_diameter(0)
print(c1.radius)


# 1. @classmethod (Class Method)
# Key Characteristics:

#     Receives the class (conventionally named cls) as its first argument

#     Can access and modify class state

#     Commonly used for alternative constructors (factory methods)

#     Bound to the class, not the instance

# When to Use:

#     When you need to create factory methods that return class instances

#     When the method needs to access or modify class-level attributes

#     When the method's behavior depends on the class rather than an instance


# 2. @staticmethod (Static Method)
# Key Characteristics:

#     Doesn't receive any special first argument (no self or cls)

#     Cannot modify class or instance state

#     Acts like a regular function but belongs to the class's namespace

#     Used when the method is logically related to the class but doesn't need access to instance/class data

# When to Use:

#     For utility functions related to the class

#     When the method doesn't need to access instance or class attributes

#     For helper methods that perform calculations or validations
