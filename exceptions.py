try:
    # with statement automatically release external resorces 
    # it will close the file regardless it has finally close or not
    # you can also open multiple files using with statements
    # opened file will be returned as file and math object
    with open('control_flow.py') as file, open(try_math.py) as math:
        print("File opened.")
        file.__enter__ # magic method
    age = int(input("Age: "))
    xfactor = 10/age
     # when code inside try block didn't run properly, 
     # statements below will run
except (ValueError, ZeroDivisionError):
    # you can specify more than one error in exepction statement 
    # so that you don't have to write it repeatedly
    print("You didn't enter a valid age")
else:
    print("No exeptions were thrown")
finally: # statements below will always run no matter the exceptions
    file.close()

# Raising Exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10/age

try:
    # without using try block the program will crash 
    # but if we handle the exeption it will only return error message 
    # and not crash
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Cost of Raising Exceptions
from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10/age

try:
    # without using try block the program will crash 
    # but if we handle the exeption it will only return error message 
    # and not crash
    calculate_xfactor(-1)
except ValueError as error:
    # pass
    print(error)
"""

print("code1 running time: ", timeit(code1, number=1000))
# output: code1 running time with exeption:  0.553295599995181
# code1 running time with pass:  0.0005508000031113625


# different approach

from timeit import timeit


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
        # None is the absence of value
    return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("running time with if statement: ", timeit(code2, number=1000))
# output: running time with if statement:  0.00024069997016340494
# USE EXCEPTION ONLY IF YOU REALLY HAVE TO
# if you use exception where the users only a few, it won't affect really bad
# however, if the program is used by many users better only use simple if statement

