"""
Why Functions?
-> without functions - repeated, messy
"""
print("Hello Rahul, Welcome!")
print("hello Priya, Welcome!")
print("Hello Arun,  Welcome!")
# with functions - clean, reusable
def welcome(name):
    print(f"Hello {name}! Welcome.")

welcome("Rahul")
welcome("Priya")
welcome("Arun")