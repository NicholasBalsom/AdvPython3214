import numpy as np

# Create 2x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)
print("Shape of matrix:", matrix.shape)
transposed_matrix = matrix.transpose()
print("Transposed Matrix:\n", transposed_matrix)
print("shape:", transposed_matrix.shape)
