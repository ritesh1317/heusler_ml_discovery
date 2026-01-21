import pandas as pd

# Load datasets
df_true = pd.read_csv("heusler_true.csv")
df_mp = pd.read_csv("heusler_mp.csv")

# Check available magnetic columns
print("MP columns:", df_mp.columns)

# Keep magnetic info
possible_cols = ["formula", "is_magnetic", "total_magnetization"]
available_cols = [c for c in possible_cols if c in df_mp.columns]

if len(available_cols) <= 1:
    raise ValueError("No magnetic columns found in heusler_mp.csv")

df_mp_mag = df_mp[available_cols].drop_duplicates(subset="formula")

# Merge
df_merged = df_true.merge(df_mp_mag, on="formula", how="left")

# Save
df_merged.to_csv("heusler_true_with_magnetism.csv", index=False)

print("Created heusler_true_with_magnetism.csv")
print("Columns:", df_merged.columns)
print("Total entries:", len(df_merged))
