import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

titanic_data = pd.read_csv("csv/newtitanic.csv")

corr = titanic_data.select_dtypes(include=["float64", "int64"]).corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap of Numeric Features")
plt.show()
