try:
     # code that MIGHT fail

    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result: ", result)
except ValueError:
    # runs if int() fails (non-numeric input)
    print("That is not a number")
except ZeroDivisionError:
    # runs if number is 0
    print("Can't divide by a zero")
except Exception as e:
# catches ANY other exception
# 'e' contains the error message
    print(f"Something went wrong: {e}")
else:
# runs ONLY if no exception occurred
    print("Everything went fine!")
finally:
 # runs ALWAYS — exception or not
 # perfect for cleanup (closing files, db connections
    print ("Done")