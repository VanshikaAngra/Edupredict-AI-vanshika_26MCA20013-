import pandas as pd

df = pd.read_excel("data/students.xlsx")

print("Excel Data:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())