squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Indexing
print(squares[0])
print(squares[-1])
print(squares[-2])
# Slicing
print(squares[-3: ])
concatenation = squares + [121,144,169,196,225]
print(concatenation)
# unlike strings which are immutable , Lists are mutable.
cubes = [1,8,27,65]
print(cubes)
print("After changing the value of cube of 4")
cubes[3] = 64
print(cubes)
# Methods of List
"""
list.append() - To add new items to the end of the list, by using list.append() method
"""
cubes.append(125)
cubes.append(6**3)
cubes.append(7**3)
cubes.append(8**3)
cubes.append(9**3)
cubes.append(10**3)
print("Cubes after adding upto 10")
print(cubes)
# Python never copies data. When we assign a list to a variable,
# the variable refers to the existing list. Any changes we make to the list through one variable will be seen through all other variables that refer to it:
rgb = ["Red", "Green","Blue"]
print(rgb)
#rgba = rgb # This does not create a new list.Both variables point to the same list object in memeory.
# In python id() returns the identity of an object - a value that uniquely identifies that object during its life time.
print(id(rgb) == id(rgba))
print(id(rgb))
print(id(rgba))
rgba.append("Alph")
print(rgb)


