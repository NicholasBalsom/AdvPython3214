import pandas as pd

# Read the csv
df = pd.read_csv("student_scores.csv")

# Calculate the average grade
average = df["Grades"].mean()

# Display the average grade
print(f"Average Grade: {average:.2f}\n")

# Filter and display the student data of those with grades > 80
print("Students with grades > 80")
print(df[df["Grades"] > 80])
