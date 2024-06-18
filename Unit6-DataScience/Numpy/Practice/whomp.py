import numpy as np

array1 = np.random.randint(0, 100, size=(4, 10))
print(array1)

mask = array1 > 70
print(mask)
print("All tests in a column are true:")
print(mask.all(axis=0))
print("\nAny test in a row is true:")
print(mask.any(axis=1))

mask = array1[0, :] >= 70  # colon indicates all columns, zero indicates row 0
print("\nShowing the mask")
print(mask)
print("\nThe mask applied to all columns")
print(array1[:, mask])  # colon represents all rows of chosen columns
