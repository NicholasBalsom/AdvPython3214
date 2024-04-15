import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("List addition:", list1 + list2)

array1 = np.array(list1)
array2 = np.array(list2)

print("Array addition:", array1 + array2)


# Dimensional Arrays

fav_numbers = [12, 10, 16]
fav_num_array = np.array(fav_numbers)

print("1-Demensional array:", fav_num_array)

matrix = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

print("2-Dimensional array:", matrix)


# Attributes


# ndim - tells you the number of dimensions of the array.
array_1d = np.array([1, 2, 3])
array_2d = np.array([[1, 2, 3], [1, 2, 3]])

print("Array 1, numner of dimensions:", array_1d.ndim)
print("Array 2, number of dimensions:", array_2d.ndim)

# shape - represents the dimensions of the array as a tuple

print("Array 1, shape:", array_1d.shape)
print("Array 2, shape:", array_2d.shape)

# size - represents the number of items in a array

print("Array 1, size:", array_1d.size)
print("Array 2, size:", array_2d.size)

# dtype - represents the data typr of elements in a array

print("Array 1, data type:", array_1d.dtype)
print("Array 2, data type:", array_2d.dtype)

# itemsize - returns the size in bytes of each item in the array

print("Array 1, item size (bytes):", array_1d.itemsize)
print("Array 2, item size (bytes):", array_2d.itemsize)


# Advanced arrays

# np.zeros - array of zeros

zeros = np.zeros(shape=(4, 4), dtype=int)
print("\nZeros array (type: int):\n", zeros)

# np.ones

ones = np.ones(shape=(5, 4), dtype=int)
print("\nOnes array (type: int):\n", ones)

# np.arange (a range not arrange)

ten_to_nineteen = np.arange(10, 19)
print("\nArray from 10 to 19:\n", ten_to_nineteen)

# High demensional arrays - reading (3-D arrays)

array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array_3d)

print("3D array shape:", array_3d.shape)
print("3D array size:", array_3d.size)
print("3D array number dimensions:", array_3d.ndim)

# ----------------location of element vvv ---- item in outermost list, item in middle list, item in that list
print("Specific Element:", array_3d[1, 1, 2])
