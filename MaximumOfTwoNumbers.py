def max(a,b):
    if a > b:
        return a
    else:
        return b
a = int(input("Enter the vakue of a: "))
b = int(input("Enter the value of b: "))
maximum = max(a,b)
print("The maximun number among the three numbers is ", maximum)