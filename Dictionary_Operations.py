d = {"a" : 1, "b" : 2, "c" : 3}
# Add/Update
d["d"] =4
d["e"] =5
d["a"] =99
# remove
d.pop("a")
print(d)
d.pop("z",None) # safe remove - no crash if missing
del d["b"] # delete key 
print(d)
d.clear()
print(d)
for key in d:
    print(key)
for key, value in d.items():
    print(f"{key} -> {value}")
for value in d.values():
    print(f"{value}")
# Check
print("name" in d)
print("email" in d)
print(len(d))