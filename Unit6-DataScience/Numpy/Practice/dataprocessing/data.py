import numpy as np

weekly_expenses = np.array([250, 300, 350, 400, 320, 280, 500])
weekly_income = np.array([1000, 1050, 990, 1200, 1100, 1150, 1300])
weekly_savings = weekly_income - weekly_expenses

print("Weekly savings:", weekly_savings)
