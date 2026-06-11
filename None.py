# None means "no value" - like an empty box.
result = None
winner = None
# Check for None - always use 'is', not '=='
if result is None:
    print("No result yet")
if winner is not None:
    print("We have a winner!")
# Functions that don't return give None
def say_hello():
    print("Hello!")
x = say_hello()
print(x)