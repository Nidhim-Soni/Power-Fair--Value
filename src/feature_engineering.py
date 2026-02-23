import pandas as pd
import os

# -----------------------
# LOAD MERGED DATA
# -----------------------
df = pd.read_csv("data/processed/germany_with_weather.csv")

df["datetime"] = pd.to_datetime(df["datetime"])

# -----------------------
# TIME FEATURES
# -----------------------
df["hour"] = df["datetime"].dt.hour
df["day_of_week"] = df["datetime"].dt.dayofweek
df["month"] = df["datetime"].dt.month
df["year"] = df["datetime"].dt.year

# -----------------------
# LAG FEATURES
# -----------------------
df["lag_24"] = df["price"].shift(24)
df["lag_48"] = df["price"].shift(48)
df["lag_168"] = df["price"].shift(168)

# remove missing rows
df = df.dropna()

# -----------------------
# SAVE
# -----------------------
os.makedirs("data/features", exist_ok=True)

df.to_csv("data/features/germany_features.csv", index=False)

print(df.head())
print("\n✅ Features rebuilt with weather.")