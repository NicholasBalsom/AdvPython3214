import pandas as pd

# Part 1: Setup and Initial exploration
df = pd.read_csv("csv/resort.csv")
df = df.set_index("SkierID")  # Set the index to the skier id

# Viewing top, bottom and random sample of entries
print(f"Top entries:\n{df.head()}")
print(f"\nBottom entries:\n{df.tail()}")
print(f"\nRandom sample:\n{df.sample(5)}")


# Part 2: Cleaning the data
print(f"Number of miising values: {df.isnull().sum()}")
most_common_weather = df["WeatherConditions"].mode()
df = df.fillna({"WeatherConditions": most_common_weather[0]})
print(f"\nFilled nan values:\n{df}")

# Remove dupelicate rows
print(f"\nDupelicate rows:\n{df.duplicated()}")
df = df.drop_duplicates()
print(f"\nDupelicate rows removed:\n{df}")


# Part 3: Basic Data Analysis
# Finding average runtime
avg_run_time = df["RunTime"].mean()
print(f"\nAverage run time:\n{avg_run_time}")

# Correlation between run time and slope difficulty
# dictonary for mapping slope difficulty values to a number
map = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3,
    "Expert": 4,
}

numerical_df = df.copy(deep=True)  # Make a copy of the dataframe so we can save the original
numerical_df["SlopeDifficulty"] = numerical_df["SlopeDifficulty"].map(map)  # Mapping slope diff to numbers
correlation = numerical_df["RunTime"].corr(numerical_df["SlopeDifficulty"])  # Calculate correlation
print(f"\nCorrelation between RunTime and SlopeDifficulty:\n{correlation:.2%}")

# Finding unique weather conditions
unique_weather = df["WeatherConditions"].unique()
print(f"\nUnique weather conditions:\n{unique_weather}")


# Part 4: Data Manipulation Skills
# Creating new performance score column
df = df.assign(PerformanceScore=numerical_df["RunTime"] - numerical_df["SlopeDifficulty"] * 10)

# Rearranging the order of columns for easy reading
df = df[["SkierName", "RunTime", "SlopeDifficulty", "PerformanceScore", "Date", "WeatherConditions"]]
print(f"\nWith new Performance Score column:\n{df}")

# Sorting the dataframe by runtime and performance score
df_sorted = df.sort_values("RunTime", ascending=True)
print(f"\nSorted by lowest Runtimes:\n{df_sorted}")
df_sorted = df.sort_values("PerformanceScore", ascending=True)
print(f"\nSorted by lowest PerformanceScores(Lower the better, like golf):\n{df_sorted}")

# Grouping the dataframe by date and weather conditions
df_groupby_date = df.groupby(["Date"]).mean(numeric_only=True)
print(f"\nGrouped by Date:\n{df_groupby_date}")
df_groupby_weather = df.groupby(["WeatherConditions"]).mean(numeric_only=True)
print(f"\nGrouped by Weather:\n{df_groupby_weather}")
