import pandas as pd

emp_data1 = {
    "Employee ID": ["E001", "E002", "E003"],
    "Name": ["Bob", "Jack", "Billy"],
    "Department": ["HR", "HR", "HR"],
    "Salary": [50000, 60000, 70000],
}

emp_data2 = {
    "Employee ID": ["E004", "E005", "E006"],
    "Name": ["Dave", "Eva", "Babatunde"],
    "Department": ["Finance", "Finace", "Finance"],
    "Salary": [80000, 90000, 99999],
}

df_employees = pd.DataFrame(emp_data1)
df_employees2 = pd.DataFrame(emp_data2)

# Concatenate two dataframes
df_employees = pd.concat([df_employees, df_employees2], ignore_index=True)

# Set index to use employee id instead of 0,1,2....
df_employees.set_index("Employee ID", inplace=True)
print(f"Original data frame:\n\n{df_employees}")

# Use a column(name) as an index for a different view
df_by_name = df_employees.set_index("Name")
print(f"\nThis is a new view with Name as index:\n\n{df_by_name}")

# Manually specify columns (including indexes)
columns = ["Employee ID", "Name", "Department", "Salary"]

# Create a new employee as a dataframe using concat
new_employee_data = pd.DataFrame([["E007", "James", "HR", 100000]], columns=columns)
new_employee_data.set_index("Employee ID", inplace=True)

# Concat the new employee to the original dataframe
df_employees = pd.concat([df_employees, new_employee_data])
print(f"\nThis is an updated view with new employee:\n\n{df_employees}")

# Drop a column
df_simple = df_employees.drop(columns=["Department"])
print("\nThis is a simple view with Dept dropped:\n")
print(df_simple)
