import pandas as pd

# load germany electricity prices
df = pd.read_csv("data/raw/Germany.csv")

# keep only required columns
df = df[["Datetime (UTC)", "Price (EUR/MWhe)"]]

# rename columns
df.columns = ["datetime", "price"]

# convert datetime to proper format
df["datetime"] = pd.to_datetime(df["datetime"])

# sort by datetime
df = df.sort_values("datetime")

# create processed folder if not exists
import os
os.makedirs("data/processed", exist_ok=True)

# save cleaned dataset
df.to_csv("data/processed/germany_prices_clean.csv", index=False)

print(df.head())
print("\nClean dataset saved successfully.")