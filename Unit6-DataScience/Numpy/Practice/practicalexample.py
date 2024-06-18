import numpy as np

data = np.array([[20, 22, 19], [30, 31, 29]])

# x = city names y = days observed
print("Daily observations:\n", data)

transposed_data = data.transpose()
print("Transposed for variable-wise operation:\n", transposed_data)

# Calculate average temperatures
average_temperatures = np.mean(transposed_data, axis=1)
print("Average temp for each city:\n", average_temperatures)
