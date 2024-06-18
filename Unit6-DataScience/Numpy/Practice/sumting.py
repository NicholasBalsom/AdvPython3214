import numpy as np

a = np.array([1, np.nan, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

result = a + b
print("Addition using operator:", result)

result_add_func = np.add(a, b)
print("Addition using function:", result_add_func)
