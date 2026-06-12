def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = list(map(int,input("enter numbers separated  by space: ").split()))
result = sum(numbers)
print("Sum of numbers in the list is ", result)
    