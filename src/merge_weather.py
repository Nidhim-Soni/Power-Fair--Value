import pandas as pd

# -----------------------
# LOAD DATA
# -----------------------
prices = pd.read_csv("data/processed/germany_prices_clean.csv")
weather = pd.read_csv("data/raw/weather_data.csv")

# convert datetime
prices["datetime"] = pd.to_datetime(prices["datetime"])

weather["utc_timestamp"] = pd.to_datetime(weather["utc_timestamp"])
weather["utc_timestamp"] = weather["utc_timestamp"].dt.tz_localize(None)

# -----------------------
# SELECT GERMANY TEMPERATURE
# -----------------------
# Germany temperature column usually looks like:
# DE_temperature

germany_weather = weather[["utc_timestamp", "DE_temperature"]]

germany_weather.columns = ["datetime", "temperature"]

# -----------------------
# MERGE DATASETS
# -----------------------
merged = pd.merge(prices, germany_weather, on="datetime", how="inner")

# -----------------------
# SAVE
# -----------------------
merged.to_csv("data/processed/germany_with_weather.csv", index=False)

print(merged.head())
print("\n✅ Weather merged successfully")