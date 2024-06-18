# Add and multiply diff-shaped arrays
import numpy as np

a1 = np.array([1, 2, 3])  # [1 2 3]
a2 = np.array([4, 5, 6])  # [4 5 6]

print(f"Array 1: {a1}\nArray2: {a2}\n")

array_sum = np.add(a1, a2)  # [5 7 9]
array_product = np.multiply(a1, a2)  # [4 10 18]

print(f"Addition: {array_sum}\nMultiplication: {array_product}\n")

# Diff shaped arrays
a1_2d = np.array([[1], [2], [3]])
a2_2d = np.array([[4], [5], [6]])

array2d_sum = np.add(a1_2d, a2_2d)
array2d_product = np.multiply(a1_2d, a2_2d)

print(f"Addition 2d:\n{array2d_sum}\n\nMultiplication 2d:\n{array2d_product}\n")
