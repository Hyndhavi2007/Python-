s = {1,2,3,4,5}
s.add(6)
s.remove(3)
s.discard(99)
print(3 in s)
a = {1,2,3,4}
b = {3,4,5,6}
print(a|b) # {1,2,3,4,5,6} - union  - all
print(a & b) # {3,4} - intersection(common)
print(a -b) # {1,2} - difference
print(a^b) # {1,2,5,6} -  symmetric difference not in both.
