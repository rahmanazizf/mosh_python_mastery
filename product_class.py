
class Product:
    """
    Set the price of a product
    """
    def __init__(self, price):
        # to set the properties or methods as private members,
        # we can write double underscore '__' to prevent accidental access
        self.price = price

    # the decorator below allows us to make a method to a property
    # therefore we don't need to deal with operator that is seemingly separated from
    # other class' methods
    @property
    def price(self):
        """
        Property of price
        """
        return self.__price
    
    @price.setter
    def price(self, value):
        """
        Take a value and storing the value into the price property.
        Parameter
        value: int/float (value > 0 otherwise it raises a ValueError) 
        """
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value



product = Product(30)
print(product.price)