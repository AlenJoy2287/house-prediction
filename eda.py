
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("house_prices.csv")

# 1. Display dataset size
print("Dataset shape:", df.shape)

# 2. Display first five rows
print("\nFirst five rows:")
print(df.head())

# 3. Check column names and data types
print("\nDataset information:")
df.info()

# 4. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 5. Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# 6. Statistical summary
print("\nStatistical summary:")
print(df.describe())

# 7. Distribution of house prices
plt.figure(figsize=(8, 5))
plt.hist(df["MedHouseVal"], bins=30, edgecolor="black")
plt.title("Distribution of Median House Values")
plt.xlabel("Median House Value (units of $100,000)")
plt.ylabel("Number of records")
plt.tight_layout()
plt.show()

# 8. Median income versus house value
plt.figure(figsize=(8, 5))
plt.scatter(df["MedInc"], df["MedHouseVal"], alpha=0.3)
plt.title("Median Income vs Median House Value")
plt.xlabel("Median Income (in tens of thousands of dollars)")
plt.ylabel("Median House Value (units of $100,000)")
plt.tight_layout()
plt.show()

print("\nEDA completed successfully!")
