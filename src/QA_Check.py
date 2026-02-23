import pandas as pd

df = pd.read_csv("data/processed/germany_prices_clean.csv")

qa_report = {
    "rows": len(df),
    "missing_values": df.isna().sum().to_dict(),
    "start_date": df["datetime"].min(),
    "end_date": df["datetime"].max(),
    "duplicate_timestamps": df["datetime"].duplicated().sum()
}

qa_df = pd.DataFrame([qa_report])

qa_df.to_csv("outputs/qa_report.csv", index=False)

print("QA report saved.")