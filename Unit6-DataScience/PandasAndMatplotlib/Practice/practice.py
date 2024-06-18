import pandas as pd

temps = pd.Series([22, 25, 28], index=["Port aux Basques", "Corner Brook", "St. Johns"])
temps2 = pd.Series([2, 3, 4], index=["Port aux Basques", "Corner Brook", "St. Johns"])

temp_sum = temps + temps2

print(f"Daytime temps:\n{temps}")
print(f"\nNightime temps:\n{temps2}")
print(f"\nSum of temps:\n{temp_sum}")


def adjust_temp(x):
    return x + 1.5  # Add 1.5 to each item


adjusted_temps = temps.apply(adjust_temp)
print(f"Adjusted grades:\n{adjusted_temps}")


data_dict = {"a": 10, "b": 20, "c": 30}
series_dict = pd.Series(data_dict)
print(f"\nDictionary series:\n{series_dict}")


high_temps = temps > 24
print(f"\nHigh temps:\n{temps[high_temps]}")

print(temps.isnull())
