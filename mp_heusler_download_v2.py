from mp_api.client import MPRester
import pandas as pd

API_KEY = "lSeobAdwYZz2JFKyd8cilECvQm8t78bC"

with MPRester(API_KEY) as mpr:
    docs = mpr.materials.summary.search(
        crystal_system="cubic",
        fields=[
            "material_id",
            "formula_pretty",
            "formation_energy_per_atom",
            "energy_above_hull",
            "band_gap",
            "is_magnetic",
            "ordering",
            "total_magnetization",
            "symmetry",
        ],
        chunk_size=1000
    )

data = []
for d in docs:
    if d.symmetry and d.symmetry.number in [216, 225]:
        data.append({
            "material_id": d.material_id,
            "formula": d.formula_pretty,
            "formation_energy": d.formation_energy_per_atom,
            "ehull": d.energy_above_hull,
            "band_gap": d.band_gap,
            "is_magnetic": d.is_magnetic,
            "magnetic_ordering": d.ordering,
            "total_magnetization": d.total_magnetization,
            "spacegroup": d.symmetry.number,
        })

df = pd.DataFrame(data)
df.to_csv("heusler_mp.csv", index=False)

print("SUCCESS!")
print("Saved heusler_mp.csv")
print("Total entries:", len(df))
