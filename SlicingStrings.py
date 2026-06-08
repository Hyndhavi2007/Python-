"""
we can return a range of characters by using the slice syntax.
By specifying the start and end index, separated by colon, to return the part of string.
The end index will not be included suppose we give 2:5 it takes 2,3,4
"""
a = "Hello, World!"
print(a[2:5])
"""
Slicing from the start: By leaving out the start index, the range will start at the first character:
"""
print(a[:8])
"""
Slicing to the end: by leaving out the end index, the range will go the end.
"""
print(a[0:])
"""
Negative indexing: use negative indexes to start the slice from enf=d of string.
"""
print(a[-5:-1])