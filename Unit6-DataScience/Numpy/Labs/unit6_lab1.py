import numpy as np

# Part 1: Indexing and Slicing

# Task 1: Accessing elements
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Task 1:\n----------------")
print("First element", arr1[0])
print("Last element:", arr1[-1])
print("5th element:", arr1[4])

# Task 2: Slicing Arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nTask 2:\n------------------")
print("First row:", arr2[0])
print("Second column:", arr2[:, 1])
sub_array = arr2[0:2, 0:2]
print("Sub array:\n", sub_array)

# Part 2: Transposing Arrays

# Task 3: Transposing a matrix
arr2_transposed = arr2.transpose()
print("\nTask 3:\n-------------------")
print("Original:\n", arr2)
print("\nTransposed:\n", arr2_transposed)


# Part 3: Array Math

# Task 4: Basic Arithmetic Operations
print("\nTask 4:\n-----------------")
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
print("Addition:")
print(a + b)
print(np.add(a, b))

print("\nSubtraction:")
print(a - b)
print(np.subtract(a, b))

print("\nMultiplication:")
print(a * b)
print(np.multiply(a, b))

print("\nDivision:")
print(a / b)
print(np.divide(a, b))

print("\nRemaider:")
print(a % b)
print(np.remainder(a, b))


# Part 4: Universal Functions

# Task 5: Exploring More universal functions
print("\nTask 5:\n------------------")
print("Square root:", np.sqrt(a))
print("Exponential:", np.exp(a))
print("Logarithm:", np.log(b))


# Additional Challenge:
array2d_a = np.array([[1, 2, 3], [5, 3, 2], [5, 6, 7]])
array2d_b = np.array([[5, 4, 2], [8, 5, 9], [3, 4, 5], [1, 2, 3]])
print("\nAdditional Challenge:\n----------------------")
print("Matrix multiplication:", np.dot(array2d_a, arr2))
print("Combining arrays:", np.concatenate((array2d_a, array2d_b), axis=0))
print("Average:", np.mean(array2d_a))
print("Median:", np.median(array2d_a))
print("Standard Deviation", np.std(array2d_a))
