import os
import pandas as pd

def clean_country(country):
    if pd.isna(country):
        return ""
    return str(country).strip().upper()

def run_pipeline():
    os.makedirs("output", exist_ok=True)
    df = pd.read_csv("data/transactions.csv")

    # 1. Data Quality Checks (Drop missing critical fields)
    df = df.dropna(subset=["transaction_id", "user_id", "transaction_date"])

    # 2. Country Cleaning
    df["country"] = df["country"].apply(clean_country)

    # 3. Amount Validation
    valid_purchase = (df["transaction_type"] == "purchase") & (df["amount"] > 0)
    valid_refund = (df["transaction_type"] == "refund") & (df["amount"] < 0)
    df = df[valid_purchase | valid_refund]

    # 4. Create Aggregated Output
    agg_df = df.groupby(["country", "transaction_date"]).agg(
        number_of_transactions=("transaction_id", "count"),
        number_of_users=("user_id", "nunique"),
        total_amount=("amount", "sum")
    ).reset_index()

    agg_df.to_csv("output/summary.csv", index=False)
    print("Pipeline executed successfully. Output saved to output/summary.csv")

if __name__ == "__main__":
    run_pipeline()
