import pandas as pd
from sklearn.metrics import mean_absolute_error

# load feature dataset
df = pd.read_csv("data/features/germany_features.csv")

# ---- TRAIN / TEST SPLIT ----
split_index = int(len(df) * 0.8)

train = df.iloc[:split_index]
test = df.iloc[split_index:]

# ---- BASELINE MODEL ----
# prediction = yesterday same hour
y_true = test["price"]
y_pred = test["lag_24"]

# evaluate
mae = mean_absolute_error(y_true, y_pred)

print("Baseline MAE:", mae)