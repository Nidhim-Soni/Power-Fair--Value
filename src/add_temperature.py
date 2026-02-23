import requests
import pandas as pd

url = (
    "https://archive-api.open-meteo.com/v1/archive?"
    "latitude=52.52&longitude=13.41"
    "&start_date=2015-01-01"
    "&end_date=2026-02-23"
    "&hourly=temperature_2m"
)

data = requests.get(url).json()

temp = pd.DataFrame({
    "datetime": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"]
})

temp.to_csv("data/raw/temperature.csv", index=False)

print("Temperature data downloaded.")