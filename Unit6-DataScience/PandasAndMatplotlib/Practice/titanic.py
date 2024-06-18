import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("csv/titanic.csv")

# Basic printing
print("Head():\n----------------")
print(data.head())
print("\nDescribe():\n----------------")
print(data.describe())
print("\nCheck for missing values:\n---------------------------")
print(data.isnull().sum())

# Handle missing data
data["Age"].fillna(data["Age"].median(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)
print("\nWith age/embarked filled in:\n----------------------")
print(data.isnull().sum())

# Change mappings of C, Q, and S to France, Ireland, England
embarked_map = {"C": "France", "Q": "Ireland", "S": "England"}
data["Embarked"] = data["Embarked"].map(embarked_map)
print("\nWith new embarked mapping:\n-----------------------------")
print(data.head())

# Adding new coulumn
print("\nNew Coulmn:\n------------------------------")
data["FamilySize"] = data["SibSp"] + data["Parch"] + 1
print("\nPrint with new coulumn")
print(data.head())

survival_by_sex = data.groupby("Sex")["Survived"].mean()
survival_by_class = data.groupby("Pclass")["Survived"].mean()
survival_by_family_size = data.groupby("FamilySize")["Survived"].mean()
print("\nSurvival by sex:\n-----------------")
print(survival_by_sex)
print("\nSurvival by class\n--------------")
print(survival_by_class)
print("\nSurvival by family size\n------------------------")
print(survival_by_family_size)

# Visualization matplotlib.pyplot
survival_by_sex.plot(kind="bar", color=["pink", "blue"])
plt.title("Survival rates by sex")
plt.xlabel("Sex")
plt.ylabel("Survival rates")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x="Pclass", y="Fare", data=data)
plt.title("Fare prices by class")
plt.xlabel("Cabin Class")
plt.ylabel("Fare price")
plt.show()
