# To append elements from another list to the current list,We use extend() method
fruits = ["apple", "banana","cherry"]
tropical = ["mango","pineapple","papaya"]
print(fruits)
print("the length of the fruits list is " ,len(fruits))
print(tropical)
print("the length of the tropical list is " , len(tropical))
fruits.extend(tropical)
print(fruits)
print("the length of the list after using extend() methos is " , len(fruits))

"""
The extend() method does not have to append lists, 
we can add any iterable object(tuples,sets, dictionaries etc.,)

"""