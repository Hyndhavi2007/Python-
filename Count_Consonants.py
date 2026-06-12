def Count_Consonants(text):
    count = 0
    for char in text:
        if char.lower() is not "aeiou":
            count += 1
    return count
text = input("Enter a string: ")
consonants = Count_Consonants(text)
print("The number of consonants in the text are " , consonants)