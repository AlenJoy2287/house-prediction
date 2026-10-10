
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Download the housing dataset
housing = fetch_california_housing(as_frame=True)

# Combine input features and house prices
df = housing.frame

# Save the dataset as a CSV file
df.to_csv("house_prices.csv", index=False)

print("Dataset downloaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())
