from datetime import date
d1 = date.fromisoformat(input("Enter the initial date (YYYY - MM - DD): "))
d2 = date.fromisoformat(input("Enter the final date(YYYY - MM - DD): "))
difference = d2 - d1
print(difference.days, "days")
