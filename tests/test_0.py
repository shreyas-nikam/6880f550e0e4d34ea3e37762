import pytest
import pandas as pd
from datetime import datetime
from definition_bd5471eca76843b2ac3a7920c5e25f43 import generate_synthetic_loss_data

def is_iso_format(date_string):
    try:
        datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return True
    except:
        return False

def validate_date_format(start_date, end_date):
    assert is_iso_format(start_date), "Start date is not in ISO format."
    assert is_iso_format(end_date), "End date is not in ISO format."

def validate_date_range(start_date, end_date):
    start = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
    end = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
    assert start <= end, "Start date must be before end date."

@pytest.mark.parametrize("num_events, start_date, end_date, business_units, risk_categories", [
    (10, "2023-01-01T00:00:00", "2023-01-10T00:00:00", ["BU1", "BU2"], ["Risk1", "Risk2"]),
    (0, "2023-02-15T00:00:00", "2023-02-20T00:00:00", ["BU3"], ["Risk3"]),
    (5, "2023-03-01T00:00:00", "2023-03-01T00:00:00", ["BU4"], ["Risk4"]),
    (3, "2023-04-05T00:00:00", "2023-04-15T00:00:00", [], []),
    (1, "2023-05-01T00:00:00", "2023-05-01T00:00:00", ["BU5"], ["Risk5"]),
])
def test_generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories):
    validate_date_format(start_date, end_date)
    validate_date_range(start_date, end_date)

    df = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)

    if num_events > 0:
        assert isinstance(df, pd.DataFrame)
        assert len(df) == num_events
        assert "Timestamp" in df.columns
        assert "Business_Unit" in df.columns
        assert "Risk_Category" in df.columns
        assert "Loss_Amount" in df.columns
        assert "Near_Miss_Flag" in df.columns
        assert "Control_Breach_Type" in df.columns
        assert "Recovery_Time_Days" in df.columns
        
        if business_units:
          assert all(item in business_units for item in df["Business_Unit"].unique())
        
        if risk_categories:
          assert all(item in risk_categories for item in df["Risk_Category"].unique())
    else:
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0
