# A dictionary stores key-value pairs — like a real dictionary where every word (key) has a meaning (value).
student = {
    "name" : "Rahul",
    "age"  : 21,
    "city"  : "hyderabad",
    "marks":  [85,99, 90]
}
print(student["name"])
print(student ["marks"])
print(student.get("email"))
print(student.get("email","N/A"))
