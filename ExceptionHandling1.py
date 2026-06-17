try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result: ", result)
except ValueError:
    print("That is not a number")
except ZeroDivisionError:
    print("Can't divide by a zero")
except Exception as e:
    print(f"Something went wrong: {e}")
else:
    print("Everything went fine!")
finally:
    print ("Done")