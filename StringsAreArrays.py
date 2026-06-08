"""
Strings in python are Arrays of unicode characters.
Python does not have a character data type, a single chararcter is simply a string with a length of 1.
"""
a = "Hello, World!"
print(a[1])
# Looping through string
"""
Since strings are arrays,. we can loop through characters in a string, with a for loop
"""
for x in "banana":
    print(x)
print(len(a))
# To check if a certain phrase or character is present in the string, we can use the keyword "in".
text = "The best things in life are free!"
if "free" in text:
    print("free" in text)
    print("Yes, 'free' is present.")
# Check if Not
    print("expensive" not in text)
if "expensive" not in text:
    print("No, expensive is NOT  present")