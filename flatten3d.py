import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array:")
print(arr)

flattened = arr.flatten()

print("\nFlattened Array:")
print(flattened)

print("\nElements Greater Than 50:")
print(flattened[flattened > 50])

print("\nEven Numbers:")
print(flattened[flattened % 2 == 0])

average = np.mean(flattened)

print("\nAverage:", average)

print("\nElements Less Than Average:")
print(flattened[flattened < average])