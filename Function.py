# If we create a variable outside a finction it is called gloabal variable.
# If we create a variable with the same name inside a function , this variable will be local , 
# and can only be used insiode the function.
# The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)