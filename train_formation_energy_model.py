import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("heusler_ml_ready.csv")

# Drop rows with missing target
df = df.dropna(subset=["formation_energy"])

# Encode Heusler type (full / half)
le = LabelEncoder()
df["heusler_type_encoded"] = le.fit_transform(df["heusler_type"])

# Features and target
features = [
    "VEC",
    "avg_d_electrons",
    "Z_mean",
    "Z_max",
    "Z_min",
    "chi_diff",
    "heusler_type_encoded"
]

X = df[features]
y = df["formation_energy"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model: Random Forest (baseline)
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== Formation Energy Model ===")
print(f"MAE (eV/atom): {mae:.3f}")
print(f"R2 score: {r2:.3f}")

# Plot predicted vs actual
plt.figure()
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])
plt.xlabel("Actual Formation Energy (eV/atom)")
plt.ylabel("Predicted Formation Energy (eV/atom)")
plt.title("Formation Energy Prediction")
plt.show()
