# Loop over a range
for i in range (5):
    print(i)
# range(start,stop, step)
for i in range (0,10):
    print(i)
for i in range (0,10,2):
    print(i)
for i in range (10, 0 , -1):
    print(i)

# Loop over a  string
for letter in "Python":
    print(letter)
fruits = ["apple", "banana","cherry"]
for fruit in fruits:
    print(fruit)
# enumerate -  to get index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)
