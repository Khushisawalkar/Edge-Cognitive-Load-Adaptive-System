import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset (simulated sensor data)
data = {
    "temp": [25, 30, 35, 28, 32, 34, 27],
    "light": [2000, 1500, 800, 1800, 900, 700, 1600],
    "motion": [1, 0, 0, 1, 0, 0, 1],
    "stress": ["LOW", "MEDIUM", "HIGH", "LOW", "HIGH", "HIGH", "LOW"]
}

df = pd.DataFrame(data)

X = df[["temp", "light", "motion"]]
y = df["stress"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully!")

# Test prediction
test = [[31, 1000, 0]]
prediction = model.predict(test)

print("Predicted Stress:", prediction[0])