# In python, every value is either truthy (behaves like true) or falsy(behaves like false) in conditions.
# Fasly values - these all act like False in if statements
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))
print(bool([])) # empty list
print(bool({})) # empty dict
# Truthy - everything else
print(bool(1))
print(bool(-1)) # any non - zero number
print(bool("Hi"))
print(bool([1,2])) # non - empty list

