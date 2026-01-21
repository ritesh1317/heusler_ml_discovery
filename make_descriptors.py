import pandas as pd
from pymatgen.core import Composition, Element

df = pd.read_csv("heusler_true_with_magnetism.csv")

# ---------- SAFE valence electron count ----------

def valence_electron_count(formula):
    comp = Composition(formula)
    vec = 0.0
    for el, amt in comp.items():
        e = Element(el)
        group = e.group
        if group is None:
            continue
        # d-block correction
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
    if not chis:
        return 0
    return max(chis) - min(chis)

# ---- Resolve magnetic labels ----
if "is_magnetic_y" in df.columns:
    df["is_magnetic"] = df["is_magnetic_y"]
elif "is_magnetic_x" in df.columns:
    df["is_magnetic"] = df["is_magnetic_x"]
elif "total_magnetization_y" in df.columns:
    df["is_magnetic"] = df["total_magnetization_y"].fillna(0).abs() > 0.01
elif "total_magnetization_x" in df.columns:
    df["is_magnetic"] = df["total_magnetization_x"].fillna(0).abs() > 0.01
else:
    raise ValueError("No magnetic information available")

# Drop rows where magnetism is still undefined
df = df.dropna(subset=["is_magnetic"])


# ---------- Compute descriptors ----------

df["VEC"] = df["formula"].apply(valence_electron_count)

df["Z_min"], df["Z_max"], df["Z_mean"] = zip(
    *df["formula"].apply(atomic_numbers)
)

df["chi_diff"] = df["formula"].apply(electronegativity_diff)

df = df.dropna(subset=["is_magnetic"])

df.to_csv("heusler_ml_ready.csv", index=False)

print("heusler_ml_ready.csv created")
print("Columns:", df.columns)
print("Rows:", len(df))
