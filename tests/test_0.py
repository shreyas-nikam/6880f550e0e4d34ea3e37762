import pytest
import pandas as pd
from datetime import datetime
from definition_ff377f77bdd84bc9bccaab617288f78b import generate_synthetic_loss_data

def test_generate_synthetic_loss_data_valid_input():
    num_events = 10
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    business_units = ["BU1", "BU2"]
    risk_categories = ["RC1", "RC2"]
    df = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == num_events
    assert "Timestamp" in df.columns
    assert "Business_Unit" in df.columns
    assert "Risk_Category" in df.columns
    assert "Loss_Amount" in df.columns
    assert "Near_Miss_Flag" in df.columns
    assert "Control_Breach_Type" in df.columns
    assert "Recovery_Time_Days" in df.columns

def test_generate_synthetic_loss_data_zero_events():
    num_events = 0
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    business_units = ["BU1", "BU2"]
    risk_categories = ["RC1", "RC2"]
    df = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0

def test_generate_synthetic_loss_data_same_start_end_date():
    num_events = 5
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 1)
    business_units = ["BU1"]
    risk_categories = ["RC1"]
    df = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == num_events
    assert all(start_date.date() <= timestamp.date() <= end_date.date() for timestamp in df['Timestamp'])

def test_generate_synthetic_loss_data_empty_business_units_categories():
    num_events = 5
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    business_units = []
    risk_categories = []
    df = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == num_events
    assert all(bu in ["BU1", "BU2", "BU3"] for bu in df['Business_Unit'])
    assert all(rc in ["RC1", "RC2", "RC3"] for rc in df['Risk_Category'])
