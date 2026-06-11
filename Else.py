# The els block runs only if loop completed without a break
for i in range(5):
    print(i)
else:
    print("Loop finished normally")

# with break -  else does not run 
for i in range(5):
    if i == 3:
        break
else:
    print("this won't print")
# practical use - searching
numbers = [2, 4,6,8,10]
target = 7
for num in numbers:
    if num == target:
        print("Found it!")
        break
else:
    print("Not found it!")
    