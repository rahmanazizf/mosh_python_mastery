# list
from importlib.util import find_spec
from os import scandir
from turtle import forward


letters = ['a', 'b', 'c', 'd']
matrix = [[1, 0], [2, 3]]
zeros_ones = [0] * 5 + [1] * 5
zeros_ones_alternating = [0, 1] *5
combined = zeros_ones + matrix
numbers = list(range(20))

# accessing items
letters[0] = letters[0].upper() #modifying item
#print(numbers[::2]) #accessing list with 2 steps so that we get even numbers
#print(numbers[::-1]) #accessing list with reversed order

#unpacking list
nums = [1, 2] + [4] * 5
first, second, *other = nums # *other takes all values but the first and second
#print(other)

#what if we only care about the first and the last element of list
another_nums = [1, 2] + [4] * 5 + [9]
first, *other_another, last = another_nums
# print(other_another)

#loop over a list
# for index, letter in enumerate(letters):
#     print(index, letter)

# adding/removing items in list

# add
letters.append('e')

# to a specific position
letters.insert(0, "-")

#remove item
letters.pop(2)

# you don't know in what index it is stored
name = "Rahman Aziz"
letters.remove('c')

# sorting list
numbers = [3, 5, 51, 60, 4]
#numbers.sort(reverse=False)
# print(sorted(numbers)) # sorted built-in function does not affect original list
# print(numbers)

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]
# .sort() method won't be able to sort this list
# therefore we need to create our new custom function

# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item) #the function sort_item is passed into method and return the price of each item
# print(items)

# lambda expression/function
# with lambda function you dont have to define a function first

items.sort(key=lambda item: item[1])

# map function
prices = list(map(lambda item: item[1], items))  # map function returns a map object which is iterable so that
# it has to be converted into list before

# filter
filtered = list(filter(lambda item: item[1] >= 10, items))
# just as similar as map function

# list comprehension
prices_lc = [item[1] for item in items]
filtered_lc = [item[1] for item in items if item[1] >= 10]
# way cleaner and performant

# tuples
point = (1, 2, 3)
x, *other = point
# tuples is used when you want to prevent accidental errors
# if you accidentally modified the list

# sets
# a collection with no duplicates
numbers = [1, 2, 2, 3, 4]
first = set(numbers)
second = {1, 5}
# print(first & second) # intersection
# print(first | second) # union
# print(second - first) # complement of second
# print(first ^ second) # symmetric difference

# set is unordered collection of items therefore can't be accessed by index

# dictionary
# collection of value pair
point = {'x': 1, 'y': 2}
# generally the keys are integers or string but there is no limitation
# for the value, it could be anything even a function!
point1 = dict(x=1, y=2) # keyword argument

# check existence in dictionary
if 'a' in point1:
    print(point1['a'])
# print(point1.get('a', 0)) # if there is no 'a' in dictionary it will return 0

# iterating over a dictionary
# for key, value in point1.items(): # unpacking tuple into two variables
#     print(key, value)

# dictionary comprehension
values = {x: x * 2 for x in range(5)}
# tuple comprehension
values_tuple = (x * 2 for x in range(5))
# print(values_tuple) # the item wont be displayed
# for x in values_tuple:
#     print(x)

# tuple is memmory-efficient since the object is not stored in memmory
# that is why it is called generator object, it only generates not stores

# comparing size between list and tuple
from sys import getsizeof
values_tuple = (x for x in range(1000000))
values_list = [x for x in range(1000)]
# print(getsizeof(values_tuple))
# print(getsizeof(values_list))

# even though we are increasing the size of range in tuple
# it won't affect the size of the tuple

# unpacking operator
# we can unpack iterable object
# take out individual value in any iterable
unpack_value = [*range(5)]
# print(*range(5)) # * pass sequential item into print function
unpack_str = [*"Hello world"]
# print(unpack_str)
first = {'x': 1}
second = {'x': 10, 'y': 2}
combined = {**first, **second, 'z': 0}
# print(combined)

# Exercise
# find the most frequently used character in the sentence below
sentence = "This is a common interview question"
sentence = [*sentence]
char_count = {}
for char in sentence:
    if char != ' ':
        char_count[char.upper()] = char_count.get(char.upper(), 0) + 1

char_count_tuple = [*char_count.items()]
most_frequent, *char_sorted = sorted(char_count_tuple, key=lambda kv: kv[1], reverse=True)
print(most_frequent)