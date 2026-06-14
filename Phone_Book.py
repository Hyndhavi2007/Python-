phonebook = {
    "Alice": "9876543210",
    "Bob"  : "9123456789",
    "Charlie": " 9000011112"
}
phonebook["Divya"]= "9555566666"
phonebook["Alice"]="9999900000"
print(phonebook)
if "kiran" in phonebook:
    print("Kiran is in phonebook.")
else:
    print("kiran is not in phonebook.")
del phonebook["Charlie"]
print(phonebook)