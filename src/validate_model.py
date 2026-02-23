import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

df = pd.read_csv("data/features/germany_features.csv")

features = [
    "hour",
    "day_of_week",
    "month",
    "lag_24",
    "lag_48",
    "lag_168",
]

X = df[features]
y = df["price"]

tscv = TimeSeriesSplit(n_splits=5)

baseline_scores = []
xgb_scores = []

for train_idx, test_idx in tscv.split(X):

    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    # Baseline
    baseline_pred = X_test["lag_24"]
    baseline_mae = mean_absolute_error(y_test, baseline_pred)
    baseline_scores.append(baseline_mae)

    # XGBoost
    model = XGBRegressor(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    xgb_mae = mean_absolute_error(y_test, preds)
    xgb_scores.append(xgb_mae)

print("Baseline MAE:", baseline_scores)
print("XGBoost MAE:", xgb_scores)

print("\nAverage Baseline:", sum(baseline_scores)/len(baseline_scores))
print("Average XGBoost:", sum(xgb_scores)/len(xgb_scores))


# The lag-24 benchmark remains highly competitive, indicating strong daily 
# seasonality in power prices. Machine learning models without additional fundamental drivers struggle to consistently 
# outperform naive persistence models.