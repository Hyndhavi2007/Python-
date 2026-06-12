def Type_Of_Number(n):
    if n % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
num = int(input("Enter a number: "))
a = Type_Of_Number(num)
print("The number is ", a)