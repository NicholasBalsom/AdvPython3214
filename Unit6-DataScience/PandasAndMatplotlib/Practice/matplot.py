import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data for FunLand Amusement Park
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Visitors": [200, 220, 150, 180, 300, 400, 350],
    "Ride_1_Rating": [4, 3, 4, 5, 3, 5, 4],
    "Ride_2_Rating": [2, 3, 2, 4, 4, 4, 3],
    "Ride_3_Rating": [5, 5, 4, 4, 5, 3, 4],
    "Snack_1_Sales": [50, 60, 40, 70, 65, 80, 90],
    "Snack_2_Sales": [55, 65, 35, 45, 85, 95, 100],
    "Weather": ["Sunny", "Cloudy", "Rainy", "Sunny", "Sunny", "Rainy", "Sunny"],
}

funland_data = pd.DataFrame(data)

# plt.figure(figsize=(10, 6))
# plt.scatter(funland_data["Day"], funland_data["Snack_1_Sales"], color="red")
# plt.xlabel("Day")
# plt.ylabel("Snack 1 Sales")
# plt.title("Relationship between day and snack 1 sales")
# plt.show()

# plt.plot(
#     funland_data["Day"],
#     funland_data["Visitors"],
#     marker="o",
#     linestyle="-.",
#     color="blue",
# )
# plt.plot(
#     funland_data["Day"],
#     funland_data["Snack_1_Sales"],
#     marker="o",
#     linestyle=":",
#     color="red",
# )
# plt.xlabel("Day of the week")
# plt.ylabel("Number of Visitors")
# plt.title("Trends for for days of the week")
# plt.legend(["Visitors", "Snack_1_Sales"])
# plt.show()

weather_counts = funland_data["Weather"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    weather_counts,
    labels=weather_counts.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["blue", "red", "gold"],
)
plt.title("Weather Conditions at Funland")
plt.show()
