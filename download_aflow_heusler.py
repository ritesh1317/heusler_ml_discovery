from aflow import *
import pandas as pd

# Connect to AFLOW
result = search(batch_size=500).filter(
    prototype="L21"
)

print("Downloading data from AFLOW...")

data = []
for entry in result:
    data.append({
        "compound": entry.species,
        "prototype": entry.prototype,
        "formation_energy": entry.enthalpy_formation_atom,
        "magnetic_moment": entry.spin_atom,
        "band_gap": entry.Egap,
        "distance_to_hull": entry.distance_to_hull
    })

df = pd.DataFrame(data)
df.to_csv("heusler_L21_aflow.csv", index=False)

print("SUCCESS!")
print("Saved as heusler_L21_aflow.csv")
print("Total compounds:", len(df))
