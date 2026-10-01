import numpy as np

arr = np.array([10, 60, 25, 75, 40, 90, 15, 55, 30, 80])

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("\nModified Array:")
print(arr)
