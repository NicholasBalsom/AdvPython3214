import numpy as np

x = np.array([1.0, 2.5, np.nan, 1.3, np.inf, 7.2])

print("input array with bad values:")  # prints input array with bad values:
print(x)  # [1.  2.5 nan 1.3 inf 7.2]

# convert to a masked array
xmasked = np.ma.masked_invalid(x)

print("masked version:")  # prints masked version:
print(xmasked)
