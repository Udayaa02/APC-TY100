import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nSum of All Elements:")
print(np.sum(arr))

print("\nSum of Each Layer:")
print(np.sum(arr, axis=(1, 2)))

print("\nSum Along Rows:")
print(np.sum(arr, axis=2))

print("\nSum Along Columns:")
print(np.sum(arr, axis=1))
