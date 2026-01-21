import pandas as pd
from pymatgen.core import Composition

df = pd.read_csv("heusler_mp.csv")

# Drop rows with missing formulas
df = df.dropna(subset=["formula"])

def is_full_or_half_heusler(formula):
    try:
        comp = Composition(formula)
        elems = list(comp.get_el_amt_dict().values())
        elems_sorted = sorted(elems)

        # Full Heusler: X2YZ
        if elems_sorted == [1, 1, 2]:
            return "full"

        # Half Heusler: XYZ
        if elems_sorted == [1, 1, 1]:
            return "half"

        return None
    except Exception:
        return None

df["heusler_type"] = df["formula"].apply(is_full_or_half_heusler)
df = df[df["heusler_type"].notna()]

df.to_csv("heusler_true.csv", index=False)

print("SUCCESS!")
print("Saved heusler_true.csv")
print("Total true Heuslers:", len(df))
print(df["heusler_type"].value_counts())
