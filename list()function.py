"""
The list() function creates a list object.
A list object is a collection which is orderd and mutable.
"""
mylist = ["apple", "banana","cherry"]
print(mylist)
print(type(mylist))
thislist = list(("apple", "banana", "cherry"))
print(thislist)
"""
here we have created 2 lists using
1. creating a list using square brackets.
2. creating a list using the list() constructor.
list() is a buit in function that creates a list.
the inner parentheses ("apple", "banana", "cherry") create a tuple
list() -> converts that tuple into a list.
"""
# list() -> A constructor that creates a list from another iterable(sucha s tuple, string, or set).
mylist[0] = "orange"
print(mylist)