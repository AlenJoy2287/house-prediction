
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# 1. Load the dataset
df = pd.read_csv("house_prices.csv")

# 2. Separate input features and target
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict house values for test data
y_pred = model.predict(X_test)

# 6. Evaluate model performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("MODEL TRAINED SUCCESSFULLY!")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

print(f"\nMean Absolute Error (MAE): {mae:.3f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
print(f"R-squared Score: {r2:.3f}")

# 7. Save the trained model
joblib.dump(model, "house_price_model.pkl")

print("\nModel saved as house_price_model.pkl")
