day = "Monday"
match day:
    case "Monday":
        print("Start of the Week!")
    case "Friday":
        print("Almost Weekend!")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:                # _ is the default (like else)
        print("Regular weekday")