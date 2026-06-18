import math
class NegativeNumberError(Exception):
    def __init__(self , number):
        super().__init__(f"Cannot find sqaure root of negative number: {number}")
        self.number = number
def square_root(n):
    if n < 0:
        raise NegativeNumberError(n)
    return math.sqrt(n)
try:
    print(square_root(25))
    print(square_root(-4))
except NegativeNumberError as e:
    print(f"Custom Error: {e}")
