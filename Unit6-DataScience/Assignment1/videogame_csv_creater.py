import random

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

# Custom list to add specific gaming words
gaming_words = ["Quest", "Battle", "Shadow", "Saga", "Fate", "Empire"]

# Generate game names
game_names = [f"{fake.word().capitalize()} {random.choice(gaming_words)}" for _ in range(100)]

# Sample data
data = {
    "Name": game_names,
    "Platform": np.random.choice(["PS4", "Xbox One", "PC", "Switch"], 100),
    "Year": np.random.randint(2000, 2023, size=100),
    "Genre": np.random.choice(["Action", "Adventure", "Sports", "Strategy", "RPG"], 100),
    "Global_Sales": np.round(np.random.rand(100) * 5, 2),  # Sales in millions
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("csv/videogames.csv", index=False)
print("Complete")
