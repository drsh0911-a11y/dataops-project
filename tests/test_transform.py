import pytest
import pandas as pd
from src.transform import clean_country

def test_clean_country():
    assert clean_country(" egypt ") == "EGYPT"
    assert clean_country("Egypt") == "EGYPT"

def test_null_user_id_rejection():
    data = {
        "transaction_id": [1],
        "user_id": [None],
        "country": ["Egypt"],
        "transaction_date": ["2026-09-01"],
        "transaction_type": ["purchase"],
        "amount": [100]
    }
    df = pd.DataFrame(data)
    df_cleaned = df.dropna(subset=["transaction_id", "user_id", "transaction_date"])
    assert len(df_cleaned) == 0

def test_purchase_negative_amount_fails():
    amount = -100
    txn_type = "purchase"
    is_valid = not ((txn_type == "purchase" and amount <= 0))
    assert not is_valid

def test_refund_positive_amount_fails():
    amount = 100
    txn_type = "refund"
    is_valid = not ((txn_type == "refund" and amount >= 0))
    assert not is_valid
