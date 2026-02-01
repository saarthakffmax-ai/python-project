# task1_student_marks.py

student_marks = {
    "Amit": 85,
    "Neha": 92,
    "Rahul": 78,
    "Priya": 88
}

name = input("Enter student name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
