import numpy as np

array = np.array([16, 20, 30, 40, 50])  # 1D array
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2D array

print(array[0])  # First element of the array
print(array2d[1, 2])  # 2nd row and 3rd column
print(array2d[1:4])  # You can slice arrays
print(array2d[:, 1])  # All second column items in all rows
