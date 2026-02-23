# European Power Fair Value Forecasting Pipeline with AI-Assisted Trading Signals

**Candidate:** Nidhim Soni
**Email:** your_email_here

---

## Objective

The goal of this case study is to build an end-to-end forecasting pipeline producing a daily fair value estimate for the German Day-Ahead electricity market and translate forecasts into tradable prompt-curve positioning.

---

## Data Ingestion & QA

Market selected: Germany (DE-LU).

Public datasets were collected containing hourly Day-Ahead prices and weather fundamentals.

QA checks implemented:

* Missing value detection
* Duplicate timestamp validation
* Continuous hourly coverage verification

All QA outputs are reproducible through automated scripts.

---

## Forecasting Approach

### Baseline Model

A Lag-24 persistence model capturing strong daily seasonality.

Baseline MAE: **21.37 €/MWh**

### Improved Model

XGBoost regression using:

* calendar features
* lagged prices
* temperature fundamentals

Validation performed using walk-forward time-series splits.

Improved Model MAE: **6.54 €/MWh**

---

## Prompt Curve Translation

Fair value defined as:

Fair Value = Predicted Price − Market Price

Trading interpretation:

* Positive spread → LONG power
* Negative spread → SHORT power
* Small spread → HOLD

The pipeline converts statistical forecasts into actionable trading signals.

---

## AI / LLM Integration

An automated AI trading assistant generates daily trader commentary based on forecast signals, reducing manual analysis.

Output example:
`outputs/ai_trader_commentary.txt`

---

## Engineering & Reproducibility

The pipeline is fully reproducible:

Data → QA → Feature Engineering → Forecasting → Trading Signal → AI Commentary

Dependencies provided in `requirements.txt`.

---

## Conclusion

This project demonstrates an end-to-end quantitative energy trading workflow combining forecasting rigor, trading interpretation, engineering reproducibility, and AI-assisted decision support.
