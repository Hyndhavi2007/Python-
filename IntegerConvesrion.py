try:
    a = int(input("Enter a value: "))
    print("You enterd:",a)
except ValueError:
    print("The entered number is not an integer")
finally:
    print("Done.")

