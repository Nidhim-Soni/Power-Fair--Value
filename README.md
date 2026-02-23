# Power-Fair -Value
# European Power Fair Value Forecast

**Name:** Nidhim Soni  
**Email:** Nidhimsoni24@gmail.com

---

## Objective
Build an end-to-end pipeline to forecast German day-ahead electricity prices and translate forecasts into tradable prompt power signals.

---

## Data Sources
- European wholesale electricity prices (Germany)
- Open Power System Data – Weather dataset

---

## Pipeline Overview
1. Data ingestion & QA checks
2. Feature engineering
3. Baseline forecasting model
4. XGBoost forecasting model
5. Validation using TimeSeriesSplit
6. Fair value estimation
7. Trading signal generation
8. AI trader commentary automation

---

## Models
### Baseline
Lag-24 persistence model.

### Improved Model
XGBoost using:
- calendar features
- lagged prices
- temperature fundamentals

---

## Trading Interpretation
Forecast deviations from market price generate LONG / SHORT positioning signals.

---

## AI Component
Automated trader commentary generator producing daily market interpretation from forecast signals.

---

## Reproducibility
Run full pipeline using scripts inside `/src`.

