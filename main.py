import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
import os

import os

clean_path = "archive/openpowerlifting.csv"

print("Wrote file to:", os.path.abspath(clean_path))
print("File size (MB):", round(os.path.getsize(clean_path) / (1024*1024), 2))

# Reload from disk and confirm row count matches what you printed
df = pd.read_csv(clean_path, low_memory=False)
print("Reloaded cleaned shape:", df.shape)

df.to_csv(clean_path, index=False)
print(f"\nSaved cleaned dataset to: {clean_path}")
print(f"Final dataset size: {df.shape[0]:,} rows")

