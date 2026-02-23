import pandas as pd

# load forecasts
df = pd.read_csv("outputs/forecast_results.csv")

# compute fair value deviation
df["fair_value_signal"] = df["predicted_price"] - df["actual_price"]

# -----------------------
# TRADING RULE
# -----------------------
threshold = 5  # €/MWh confidence level

df["position"] = "HOLD"

df.loc[df["fair_value_signal"] > threshold, "position"] = "LONG"
df.loc[df["fair_value_signal"] < -threshold, "position"] = "SHORT"

# save results
df.to_csv("outputs/trading_signal.csv", index=False)

print(df.head())
print("\nTrading signal created.")