# Variables that are created outside the function are called Global Variables
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
