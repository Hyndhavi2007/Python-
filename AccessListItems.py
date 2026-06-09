# List items are indexed and can be accessed them by referring to the index number:
fruits = ["Apple", "Banana","Cherry", "Durain"]
print(fruits[0])
# Negative Indexing: negative indexing means start from end.
print(fruits[-3])
# range of Indexex: we can specify the range of indexes by specifying where to start and where to end the range
print(fruits[0:3])
# The search will start at 0 and end at index 3 which is not included, we get 0,1,2 index values
print(fruits[-3:-2])
# To check if item exists
"""
To check if a specified item is present in a list, we use 'in' keyword
"""
if "Apple" in fruits:
    print("Yes, apple is present in the fruit list")
else:
    print("No, apple is not present in the list")


