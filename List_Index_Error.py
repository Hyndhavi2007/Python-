try:
    list = [0,1,2,3,4,5,6,7,8,9]
    print("the length of the list is ", len(list))
    index = int(input("Enter an index:  "))
    print(f"Element at index", index, "is" , list[index])
except IndexError:
    print("The index is out of range.")
finally:
    print("Done.")