a = {1,4,9,16,25}
b = {1,8,27,64,125}
print("The union of two sets is " , a|b)
print("the intersection of two sets is ", a&b)
print("The difference between sets is ", a - b)
print("The symmetric difference between the two sets is ", a^b)
if a.issubset(b):
    print("a is subset of b")
else:
    print("a is not subset of b")