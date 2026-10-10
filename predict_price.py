
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("house_price_model.pkl")

print("===== HOUSE PRICE PREDICTION =====")

# Get house details from the user
print("\nEnter the following house details:")

med_inc = float(input("Median income (dataset units): "))
house_age = float(input("Median house age (years): "))
ave_rooms = float(input("Average rooms: "))
ave_bedrms = float(input("Average bedrooms: "))
population = float(input("Population in the area: "))
ave_occup = float(input("Average occupants per household: "))
latitude = float(input("Latitude (California dataset): "))
longitude = float(input("Longitude (California dataset): "))

# Prepare input in the same column order as training
features = pd.DataFrame([{
    "MedInc": med_inc,
    "HouseAge": house_age,
    "AveRooms": ave_rooms,
    "AveBedrms": ave_bedrms,
    "Population": population,
    "AveOccup": ave_occup,
    "Latitude": latitude,
    "Longitude": longitude
}])

# Predict
predicted_value = model.predict(features)[0]

# Dataset target is in units of $100,000
predicted_dollars = predicted_value * 100000

print("\n===== PREDICTION RESULT =====")
print(f"Predicted median house value: ${predicted_dollars:,.2f}")
print("\nNote: This model uses California housing data.")
print("It estimates a regional median value, not an exact sale price.")
