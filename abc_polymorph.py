from abc import ABC, abstractmethod

class UIControl(ABC):
    """
    Abstract method decorator turns an ordinary method into an abstract method. It means that
    we cannot instantiate (make an instance) of this class instead we have to implement (define what the abstract
    method does) in child-classes. If we do not implement/define the abstract method in parent-class, 
    the child classes derived from its parent-classes will be regarded as abstract methods too.
    In other words, an abstract method provides a contract the child-classes should follow.
    """
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

ddl = DropDownList()
txb = TextBox()


"""
Polymorphism (Many forms)

inheritance allows us to share certain methods to child-classes.

in draw method we use below, it can result in many different from depending on what implementation of draw method
in each classes.

However, since python is dynamically-typed, means that the same variable could be assigned different values
as the program runs.

Dynamically-typed ~ last-in last-out
"""
def draw(controls):
    for control in controls:
        control.draw()

draw([ddl, txb])