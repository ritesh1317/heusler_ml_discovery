from pymatgen.ext.matproj import MPRester
import pandas as pd

API_KEY = "lSeobAdwYZz2JFKyd8cilECvQm8t78bC"

with MPRester(API_KEY) as mpr:
    docs = mpr.materials.summary.search(
        fields=[
            "material_id",
            "formula_pretty",
            "formation_energy_per_atom",
            "energy_above_hull",
            "band_gap",
            "magnetic_ordering",
            "spacegroup"
        ]
    )

data = []
for d in docs:
    # Keep only cubic Heusler-relevant space groups
    if d.spacegroup and d.spacegroup.number in [216, 225]:
        data.append({
            "material_id": d.material_id,
            "formula": d.formula_pretty,
            "formation_energy": d.formation_energy_per_atom,
            "ehull": d.energy_above_hull,
            "band_gap": d.band_gap,
            "magnetic_ordering": d.magnetic_ordering,
            "spacegroup": d.spacegroup.number
        })

df = pd.DataFrame(data)
df.to_csv("heusler_mp.csv", index=False)

print("SUCCESS!")
print("Saved heusler_mp.csv")
print("Total entries:", len(df))
