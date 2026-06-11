# break - exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - skip current iteratiomn, keep going
for i in range(10):
    if i % 2 == 0:
        continue        # skips the even numbers
    print(i)            # prints odd numbers
#pass - do nothing (place holder)
for i in range(5):
    pass


