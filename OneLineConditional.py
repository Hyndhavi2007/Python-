# Ternary operator
age = 20
# normal way
if age == 20:
    print("Adult")
else:
    print("Minor")

# One- liner(ternary)
status = "Adult" if age >= 18 else "Minor"
print(status)