import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load an image as a NumPy array
img = np.array(Image.open("images/niglet.jpg"))

# Transpose the image(swap rows and columns)
img_transposed = img.transpose((1, 0, 2))

# Reverse the order of the elements in each row (90 degrees)
img_rotated = np.flip(img_transposed, axis=0)

# Display original and rotated image
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.title("Original Image")
plt.imshow(img)
plt.axis("on")

plt.subplot(122)
plt.title("Rotated image")
plt.imshow(img_rotated)
plt.axis("on")

plt.show()
