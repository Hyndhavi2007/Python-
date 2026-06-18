def divide():
    
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        result = a/b
        print("The result is ", result)
        return result
    except ZeroDivisionError:
        print("Can't Divide with Zero!")
    finally:
        print("Done.")
divide()