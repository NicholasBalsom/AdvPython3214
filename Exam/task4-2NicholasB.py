import matplotlib.pyplot as plt

# Sample data
data = {"Product A": 100, "Product B": 150, "Product C": 200}

# Plot the data
plt.bar(data.keys(), data.values())
plt.title("Sample Sales Data")
plt.xlabel("Sample Products")
plt.ylabel("Sales")
plt.show()
