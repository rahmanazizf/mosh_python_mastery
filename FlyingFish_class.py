"""
MULTIPLE INHERITANCES

An object can inherit several methods or properties from one or more parent-classes.
This method work well if we ensure that the parent-classes passing on methods or properties
do not share any common methods/properties.
"""

class Flyer:
    def fly(self):
        print("fly")

class Swimmer:
    def swim(self):
        print("swim")

class FlyingSwimmer(Flyer, Swimmer):
    pass

flyswim = FlyingSwimmer()
flyswim.fly()