import numpy as np

# daily observations of temperatures row = day, column = city
data = np.array([[32, 40, 23], [24, 29, 31], [21, 19, 25], [37, 22, 15]])

transposed_data = data.transpose()

print(np.mean(data, axis=1))
