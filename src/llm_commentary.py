import pandas as pd

# load trading signal
df = pd.read_csv("outputs/trading_signal.csv")

# summarize latest signal
latest = df.iloc[-1]

signal = latest["fair_value_signal"]
position = latest["position"]

# simple automated commentary
if position == "LONG":
    commentary = f"Model indicates bullish power prices with fair value spread of {signal:.2f} €/MWh."
elif position == "SHORT":
    commentary = f"Model indicates bearish power prices with fair value spread of {signal:.2f} €/MWh."
else:
    commentary = "No strong trading signal detected."

# save commentary
with open("outputs/ai_trader_commentary.txt", "w") as f:
    f.write(commentary)

print(commentary)