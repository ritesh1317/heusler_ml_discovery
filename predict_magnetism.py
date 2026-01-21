import sys
import joblib
import pandas as pd
from pymatgen.core import Composition, Element

# -------- Descriptor functions --------

def valence_electron_count(formula):
    comp = Composition(formula)
    vec = 0.0
    for el, amt in comp.items():
        e = Element(el)
        group = e.group
        if group is None:
            continue
        if e.block == "d":
            ve = group - 10
        elif e.block == "f":
            ve = group - 24
        else:
            ve = group
        vec += ve * amt
    return vec

def atomic_numbers(formula):
    comp = Composition(formula)
    Z = [Element(el).Z for el in comp.elements]
    return min(Z), max(Z), sum(Z)/len(Z)

def electronegativity_diff(formula):
    comp = Composition(formula)
    chis = [Element(el).X for el in comp.elements if Element(el).X is not None]
    return max(chis) - min(chis)

# -------- Main --------

if len(sys.argv) != 2:
    print("Usage: python predict_magnetism.py <FORMULA>")
    sys.exit(1)

formula = sys.argv[1]

# Build feature row
VEC = valence_electron_count(formula)
Z_min, Z_max, Z_mean = atomic_numbers(formula)
chi_diff = electronegativity_diff(formula)

X = pd.DataFrame([{
    "VEC": VEC,
    "Z_mean": Z_mean,
    "Z_max": Z_max,
    "Z_min": Z_min,
    "chi_diff": chi_diff
}])

# Load model
model = joblib.load("magnetism_model.pkl")

pred = model.predict(X)[0]
prob = model.predict_proba(X)[0]

print(f"\nFormula: {formula}")
print("Prediction:", "MAGNETIC" if pred else "NON-MAGNETIC")
print("Probability [Non-magnetic, Magnetic]:", prob)
