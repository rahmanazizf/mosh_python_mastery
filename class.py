class Point:
    
    # class level attribute
    default_color = 'red' # this attribute is shared for all instances of this class, no matter the object is the default color will be red 
    # but the value can still be changed
    
    def __init__(self, x, y):
        # these are instant attributes
        # every object can have different values of instant objects
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw_point(self):
        print(f"{self.x}, {self.y}")

    # magic method for comparing attributes
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    # magic method for performing arithmetic operations
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x*other.x, self.y*other.y)


# point1 = Point(10, 20)
# point2 = Point(15, 25)
# mult = point1 * point2

####################################

# magic method in class


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags[tag]

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
textt = "Programming is fun, but at the same time, programming is difficult"
text_list = textt.split()

for word in text_list:
    cloud.add(word)

print(cloud.__dict__)
