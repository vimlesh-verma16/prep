# Polymorphism
#     Create two classes Cat and Dog with a method speak(). Use a loop to call speak() for both objects.


class Dog:
    def speak(self):
        print("bow bow")


class Cat:
    def speak(self):
        print("mew mew")


for obj in [Cat(), Dog()]:
    obj.speak()

# Why This Demonstrates Polymorphism

#     Same Interface: Both classes have a speak() method with the same name
#     Different Implementations: Each class implements speak() differently
#     Uniform Treatment: The loop treats all objects the same way, regardless of their actual class

# Key Polymorphism Concepts Illustrated

#     Duck Typing: Python doesn't care about the object's type, only that it has a speak() method
#     Late Binding: The specific speak() implementation is determined at runtime
#     Interface Consistency: Different objects respond to the same method call
