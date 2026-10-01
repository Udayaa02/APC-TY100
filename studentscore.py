import numpy as np

marks = np.array([
    65, 78, 82, 90, 55,
    72, 88, 95, 68, 76,
    85, 91, 60, 74, 80,
    89, 70, 93, 66, 84
])

average = np.mean(marks)

print("Marks:")
print(marks)

print("\nClass Average:", average)

print("\nStudents Scoring Above Average:")
print(marks[marks > average])
