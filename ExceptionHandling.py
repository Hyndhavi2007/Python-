"""
When something goes wrong, Python raises an exception.
Without handling it, your program crashes.With handling,
you control what happens.
"""
age = int(input("Enter age: "))

try:
    age = int(input("Enter age: "))
    print("Your age is", age)
except ValueError:
    print("Please enter a valid number") 