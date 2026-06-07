# As we know that when we create a variable inside a function ,
# the variable is local variable, and can only be used inside a function
"""
To create a  global variable inside a function ,
we use the "global" keyword.
"""
def myfunc():
    global x 
    x = "fantastic"
myfunc()
print("Python is " + x)