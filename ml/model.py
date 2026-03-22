import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    "temp": [25, 30, 35, 28, 32],
    "light": [2000, 1500, 800, 1800, 900],
    "motion": [1, 0, 0, 1, 0],
    "stress": ["LOW", "MEDIUM", "HIGH", "LOW", "HIGH"]
}

df = pd.DataFrame(data)

X = df[["temp", "light", "motion"]]
y = df["stress"]

model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully")

test = [[31, 1000, 0]]
print("Prediction:", model.predict(test))