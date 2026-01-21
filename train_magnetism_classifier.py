import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("heusler_ml_ready.csv")

# ---- Define features and target ----
features = ["VEC", "Z_mean", "Z_max", "Z_min", "chi_diff"]
target = "is_magnetic"

print("Using features:", features)
print("Available columns:", df.columns)

# Drop rows with missing values
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\n=== Magnetism Classifier ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.imshow(cm)
plt.title("Magnetism Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.colorbar()
plt.show()

import joblib

joblib.dump(model, "magnetism_model.pkl")
print("Model saved as magnetism_model.pkl")

