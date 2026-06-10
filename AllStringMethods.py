s = " Hello, World! "
# Case
print(s.upper())        
print(s.lower())
print(s.title())
# Cleaning
print(s.strip()) # removes spaces from both the ends
print(s.lstrip()) # left only
print(s.rstrip())# right only
# Searching
# find() method is used to search for a substring inside a string.
# string.find(substring, start, end) 
# substring -> The text to search for
# start -> Starting index for the search(optional)
# end -> Ending index for the search(optional).
# It returns the index of the first occurence of the substring
# Returns -1 if the substring is not found.
print(s.find("World")) 
print("World" in s)
print(s.count("l"))
print(s.startswith(" H"))
print(s.endswith("! "))
# Modifying
print(s.replace("World", "Python"))
print(s.strip().split(", "))
# Joining a list into string
words = ["I", "love", "Python"]
print(" ".join(words))
print("-".join(words))
