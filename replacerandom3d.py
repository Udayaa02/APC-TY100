import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("\nModified Array:")
print(arr)