"""
[Inheritance]

When we work with a number of different classes that shares the same methods or properties,
we should not repeat ourselves by writing it in every single classes repeatedly.
Alternatively, we can pass the methods or properties on to other classes. This paradigm is known as
DRY which stands for "Don't Repeat Yourself".

At the moment we have one or more issue to fix with certain properties or methods, we just need to
work on the parent class.
"""


class Animal:
    """
    Parent/Base-class of Mammal and Fish
    """
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):

    """
    Child/Sub-class of Animal
    """
    def walk(self):
        print("walk")

class Fish(Animal):
    """
    Child/Sub-class of Animal
    """
    def swim(self):
        print("swim")



fish1 = Fish()
print(fish1.eat())