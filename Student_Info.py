students = {
    "Alice" : {"age" : 15, "grade" : 'A'},
    "Bob"   :  {"age" : 16, "grade" : 'B'},
    "Charlie" : {"age": 14,"grade": 'A+'}
}
students["Alice"]["age"] = 16
print(students["Alice"]["age"])
for student_info, student_data in students.items():
    print(f"{student_info}: {student_data["age"]} - {student_data['grade']}")
