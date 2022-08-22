from itertools import product


def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


# 1- perform a task
# 2- calculate and return a value

def get_greeting(name):
    return f"Hi, {name}"

message = get_greeting("Aziz")
print(message)

# keywords argument
def increment(number, by):
    return number + by

print(increment(2, by=1)) #keyword argument makes our code more readable

#default argument
def increment1(number, by=1):
    return number + by

#default argument allows us not pass certain arguments into our function
#but we can  still specify the argument of default argument
print(increment1(2, by=5))

# *args
def multiply(x, y):
    return x * y

#the function above only takes two arguments
#what if we want to pass more than two arguments into our funciton
# *args come to the rescue

def multiply_mod(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

#print(multiply_mod(5,4,3,2,1))
#arguments were stored in tupple data structure
#we can iterate *args that we passed into our function

# **args
def save_user(**user):
    print(user)

save_user(id=1, name='Aziz', age=23)
#when we use **args our function will packed our key-value pairs arguments into a dictionary

# scope
#a region of the code where the variable is defined
# 1- global variable
# 2- local variable

# debugging

def multiply_debug(*numbers):
    product = 1
    for number in numbers:
        product *= number
        return product

print(multiply_debug(1, 2, 3))
# multiply_debug

# Exercise
# FizzBuzz algorithm

def fizz_buzz(input):
    #more specific condition should be in the top position
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    
    return input

print(fizz_buzz(6))