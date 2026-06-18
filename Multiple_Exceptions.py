def Multiple_Exceptions():
    try:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        a = int(a)
        b = int(b)
        result = a/b
        print("The result of this t wo numbers is ",result)
    except ValueError:
        print("Value Error: Please enter integers.")
    except ZeroDivisionError:
        print("Zero Division Error: Can't Divide with Zero!")
    finally:
        print("Done.")
Multiple_Exceptions()
