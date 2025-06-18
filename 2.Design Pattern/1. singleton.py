# Singleton Using __new__ Method:


# The Singleton pattern is a design pattern that ensures a class has only one instance and provides a global point of access to that instance.
# It is commonly used when exactly one object is needed to coordinate actions across a system, such as a configuration manager, logging service, or database connection pool.

# Key Characteristics of the Singleton Pattern:
# 1. Single Instance: Only one instance of the class is created throughout the program's lifecycle.
# 2. Global Access: The single instance is globally accessible, typically through a static method or property.
# 3. Controlled Instantiation: The class controls its own instantiation to ensure no additional instances are created.

# Benefits of the Singleton Pattern:
# Controlled Access: Ensures only one instance exists, which can be useful for managing shared resources.
# Global State: Provides a single point of access to shared data or functionality.
# Lazy Initialization: The instance is created only when it is needed.

# Drawbacks of the Singleton Pattern:
# Global State: Can make code harder to test and debug due to hidden dependencies.
# Concurrency Issues: In multithreaded environments, care must be taken to ensure thread safety when creating the instance.
# Violation of SRP: The Singleton class often handles both its core functionality and the responsibility of ensuring a single instance, which can violate the Single Responsibility Principle.

# When to Use the Singleton Pattern:
# When you need exactly one instance of a class to coordinate actions (e.g., logging, configuration management).
# When you want to control access to a shared resource.


class Singleton:
    _instance = None
    _initialized = False  # Class-level flag (more explicit than instance-level)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not Singleton._initialized:
            self.value = value
            Singleton._initialized = True


# Usage
obj1 = Singleton(10)
obj2 = Singleton(20)

print(obj1.value)  # Output: 10
print(obj2.value)  # Output: 10 (same instance as obj1)
print(obj1 is obj2)  # Output: True
# ---------------------------------------------------------------------
