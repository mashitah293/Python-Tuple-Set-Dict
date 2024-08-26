#Task 3: Dict

student_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}

print(f"Bob's grade: {student_grades['Bob']}")

student_grades["Eve"] = 88
print(student_grades)

student_grades.update({"Alice": 95})
print(student_grades) 

removed_grade = student_grades.pop("Charlie")
print(student_grades)

# Loop through the dictionary and print each student's name and grade
for name, grade in student_grades.items():
    print(f"Student: {name}, Grade: {grade}")
