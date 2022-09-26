# Class: a blueprint for creating objects
# Objects: instances of a class

# Example
# Class -> Human
# Object -> John, Marry, Mosh

class Point:
    # to name a class the first letter coming should be uppercase
    # and there should not be any underscore like naming variables
    """
    A class to define a couple of points

    Attribute:
    default_color = 'red'
    """
    default_color = 'red' # class attribute is shared accross all Point objects

    def __init__(self, x, y):
        """
        [Constructor] a magic method storing attributes for an object

        Parameters:
        self: reference to the current object
        x: int (x point)
        y: int (y point)

        Since python is dynamically typed like JavaScript, attributes of an object can be stated
        after an object is created. Furthermore, we can add a new instance attribute
        that has not been created in a class.
        Example:
        point = Point()
        point.x, point.y = 3, 4
        point.z = 5
        """
        self.x = x
        self.y = y

    @classmethod # decorator, a statement adding specific functionality to a method
    def zero(cls):
        """
        Class method/Factory method

        A method shared across all objects and
        returns default values of x and y attributes.
        """
        return cls(0, 0)

    def draw(self):
        """
        Returns x and y coordinate for a Point object
        """
        print(f"Point ({self.x}, {self.y})")

    def __str__(self):
        """
        An instance of magic method

        Magic method is a method that is automatically created and called whenever
        an object is defined. More about magic method visit https://rszalski.github.io/magicmethods/

        This magic method returns x and y coordinate in string
        """
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        """
        [Magic method] Equality
        To inspect if two objects are equal with '==' operator.

        Two params required
        self: reference to the current object
        other: another object
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """
        [Magic method to support arithmetic ops] Addition

        Returns the object result of addition operations with '+'
        operator. Since in this class __str__ is defined, the result will come out as a string.
        """
        return Point(self.x + other.x, self.y + other.y)

# assign an object into a variable
point1 = Point(3, 4)
point2 = Point(3, 4)
# point = Point.zero()
print(point1.draw())

# isintance is a builtin function to investigate if an instance belongs to a certain class
print(isinstance(point1, Point))

print(point1 + point2)