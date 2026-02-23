import pandas as pd
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

# load feature dataset
df = pd.read_csv("data/features/germany_features.csv")

# ---- FEATURES & TARGET ----
features = [
    "temperature",   # NEW fundamental driver
    "hour",
    "day_of_week",
    "month",
    "lag_24",
    "lag_48",
    "lag_168",
]

X = df[features]
y = df["price"]

# ---- TRAIN / TEST SPLIT (TIME SERIES) ----
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# ---- MODEL ----
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
)

model.fit(X_train, y_train)
# ----- TRAIN PERFORMANCE -----
train_preds = model.predict(X_train)
train_mae = mean_absolute_error(y_train, train_preds)

# ---- PREDICTION ----
preds = model.predict(X_test)

# ---- EVALUATION ----
mae = mean_absolute_error(y_test, preds)
print("Train MAE:", train_mae)
print("Test MAE :",mae)

# ---- SAVE PREDICTIONS ----
forecast = pd.DataFrame({
    "actual_price": y_test.values,
    "predicted_price": preds
})

forecast.to_csv("outputs/forecast_results.csv", index=False)

print("Forecast saved.")