"""
To change the value of a specific item, we refer to the index number:
"""
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
fruits[1] = "Blackberry"
print(fruits)
fruits = ["Apple", "Blackberry","Cherry", "Durain", "Kiwi", "Watermelon","Mango"]
print(fruits)
fruits[1:3] = ["Blueberry", "Orange"]
print(fruits)
fruits[1:4] = ["Strawberry", "Pineapple", " Dragon fruit"]
print(fruits)
# If we insert more items than we replace, the new items will be inserted where we specified, and the remaining will move accprdingly.
fruits = ["apple","banana","cherry"]
fruits[1:2] = ["Blackcurrant", "Watermelon"]
print(fruits)
# The length of the list will change when the number of items inserted does not match the number of items replaced.
