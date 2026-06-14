students = {
    "s001": {"name": "Rahul", "marks": 85,"city": "Hyderabad" },
    "s002": {"name": "Priya", "marks": 92,"city": "Mumbai"} ,
    "s003": {"name": "Arun", "marks": 78, "city": "Chennai"}
}
# Access nested value
print(students["s002"]["name"])
print(students["s001"]["marks"])
# Loop through nested dict
for sid, info in students.items():
    print(f"{sid}: {info['name']} -{info['marks']}")