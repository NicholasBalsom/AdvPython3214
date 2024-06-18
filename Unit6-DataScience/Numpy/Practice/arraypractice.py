import numpy as np

array = np.array([30, 40, 50, 10, 20])  # 1D array
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2D array

print(array[0])  # First element of the array
print(array2d[1, 2])  # 2nd row and 3rd column
print(array2d[1:4])  # You can slice arrays
print(array2d[:, 1])  # All second column items in all rows


print(np.mean(array))  # calculate average
print(np.std(array))  # compute standard deviation
print(np.var(array))  # Compute variance
print(np.sort(array))  # sort array
print(np.argsort(array))  # indexs of items after sorted
# print(np.)
