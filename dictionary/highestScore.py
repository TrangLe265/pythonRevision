"""
Given a list of students and scores, find the student with the highest score [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
"""
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Edmund", 100)]
max_score = 0
student_with_max_score = ""
for student in students:
    name,score = student
    if score > max_score:
        max_score, student_with_max_score = score, name
    
print(f"Student with the highest score is {student_with_max_score} with the score of {max_score}")

