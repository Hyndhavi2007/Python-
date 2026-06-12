def Count_Vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count
text = input("Enter a string: ")
vowels = Count_Vowels(text)
print("number of vowels = ", vowels)