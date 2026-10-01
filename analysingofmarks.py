import numpy as np

marks = np.array([85, 72, 90, 65, 78, 88, 92, 70, 81, 95])

print("Marks:", marks)

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))