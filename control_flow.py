name = input("Please fill out your name : ")
print(f"Hello, {name[:name.find(' ')]}! Nice to meet you!\n")
print("Next you need to enter your age so that we can decide whether you are eligible or not")

age = int(input("Your age: "))
message = "Eligible" if age >= 18 else "not eligible" #ternary operator
print(f"You are {message}")

##########################
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# age should be between 18 and 65
age = 23
# if 18 <= age < 65:
#     print("Eligible")
# else:
#     print("Not eligible")

#shorter version (ternary operator)
age = int(input("Your age: "))
eligible_or_not = "Eligible" if 18 <= age < 65 else "Not eligible"
print(eligible_or_not)

# for loops
# successful = False
# for number in range(1, 10, 2):
#     print("Attempt", number, (number) * ".")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attemted 6 times and failed")

# Nested loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# iterables
# print(type(range(4)))
class ShoppingCart:
    def __init__(self, cart):
        self.cart = cart
    def __iter__(self):
        return iter(self.cart)

shopping_cart = ShoppingCart(['mango', 'orange', 'grape'])
for content in shopping_cart:
    print(content)

# while loop
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         print("True")
#         break

# Exercise
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")