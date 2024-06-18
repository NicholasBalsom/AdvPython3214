import pandas as pd

# Load the csv file
df = pd.read_csv("csv/Leaderboard.csv")
print(df)

# Display the first few rows of the data frame
print(f"Head:\n{df.head()}")

# Display the last few rows of the dataframe
print(f"\nTail:\n{df.tail()}")

# Display basic info about the dataframe
print(f"\nBasic info:\n{df.info()}")

# Describe dataframe
print(f"\nDescribe the data frame:\n{df.describe()}")

# Random sample of data
print(f"\nRandom 5 item sample:\n{df.sample(5)}")

# Null values and data types
print(f"\nNull values:\n{df.isnull().sum()}")
print(f"\nData Types:\n{df.dtypes}")

# Drop rows with missing data
df_clean = df.dropna()
print(f"\nCleaned dataframe(no missing values):\n{df_clean}")

# Unique
print(f"\nUnique values:\n{df.nunique().sum()}")

# Dupelicated
print(f"Dupelicated values:\n{df.duplicated().sum()}")

# Correlation Matrix (The closer to 1.0 a value is the stronger the correlation is, ex. Score relates to a longer game time)
print(f"\nCorrelation matrix:\n{df.corr(numeric_only=True)}")

print(f"\nColumns:\n{df.columns}")
print(f"\nMemory usage:\n{df.memory_usage()}")

lrg = df.nlargest(2, "GameTime")
print(f"\nLargest gametime value:\n{lrg}")
smol = df.nsmallest(2, "Score")
print(f"\nSmalest scores:\n{smol}")

print(f"\nValue_counts():\n{df.value_counts()}")
