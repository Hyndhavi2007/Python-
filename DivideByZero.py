"""
Exception handling lets us gracefully mamage runtime errors instead of letting our programs crash.
"""
try:
    a = int(input("Enter a Number: "))
    result = 10 / a
    print("The result is ", result)
except ZeroDivisionError:
    print("Can't divide by zero!")