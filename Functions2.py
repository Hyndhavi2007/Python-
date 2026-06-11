def add(a,b):
    return a +b
print(add(3,5))
# print(add(3) -> throws an error
def sub(a,b):
    if a > b:
        return a - b
    else:
        return b-a
print(sub(10,5))
print(sub(2,3))
def product(a,b):
    return (a * b)
print(product(3,7))

def div(a,b):
    return a%b , a/b
print("The remainder and the quotient is " , div(10,3))