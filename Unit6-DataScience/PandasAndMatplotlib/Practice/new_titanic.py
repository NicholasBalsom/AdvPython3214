import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic_data = pd.read_csv("csv/newtitanic.csv")

class_counts = titanic_data["Pclass"].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(class_counts.index, class_counts.values, color="skyblue")
plt.title("Passenger distribution by ticket class")
plt.xlabel("Ticket Class")
plt.ylabel("Number of Passengers")
plt.xticks([1, 2, 3], ["1st class", "2nd Class", "3rd CLass"])
plt.show()


plt.figure(figsize=(10, 6))
plt.hist(titanic_data["Age"].dropna(), bins=30, color="purple", alpha=0.7)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(titanic_data["Age"], titanic_data["Fare"], alpha=0.5)
plt.title("Age vs Fare Paid")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()


titanic_data.boxplot(column="Fare", by="Pclass", figsize=(10, 6))
plt.title("Fare distribution by ticket class")
plt.xlabel("Ticket Class")
plt.ylabel("Fare")
plt.show()


survival_counts = titanic_data.groupby(["Pclass", "Sex"])["Survived"].mean().unstack()
survival_counts.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Survival Rates by Class and Sex")
plt.xlabel("Ticket Class")
plt.ylabel("Survival rates")
plt.xticks(rotation=0)
plt.legend(title="Sex")
plt.show()


embark_counts = titanic_data["Embarked"].value_counts
plt.figure(figsize=(10, 6))
plt.pie(
    embark_counts,
    labels=embark_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["gold", "blue", "green"],
)
plt.title("Proportion of Passengers by embebarkment point")
plt.show()
