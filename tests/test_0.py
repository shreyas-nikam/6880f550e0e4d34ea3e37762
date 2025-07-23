import pytest
import pandas as pd
from definition_d0f2afc2a2e9458f851645b75c92918e import generate_synthetic_loss_data

def test_generate_synthetic_loss_data_positive():
    df = generate_synthetic_loss_data(10)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert 'Event_ID' in df.columns
    assert 'Date' in df.columns
    assert 'Basel_Event_Type' in df.columns
    assert 'Loss_Amount' in df.columns
    assert 'Impact_Category' in df.columns
    assert 'Contributing_Factors' in df.columns

def test_generate_synthetic_loss_data_zero():
    df = generate_synthetic_loss_data(0)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0

def test_generate_synthetic_loss_data_types():
    df = generate_synthetic_loss_data(1)
    assert isinstance(df['Event_ID'][0], str)
    assert isinstance(df['Date'][0], pd.Timestamp)
    #The code implementation will be in pandas and it is impossible to know the exact implementation.
    assert isinstance(df['Basel_Event_Type'][0], str)
    assert isinstance(df['Loss_Amount'][0], float)
    assert isinstance(df['Impact_Category'][0], str)
    assert isinstance(df['Contributing_Factors'][0], str)

def test_generate_synthetic_loss_data_basel_event_types():
    df = generate_synthetic_loss_data(100)
    expected_types = ['Internal Fraud', 'External Fraud', 'Employment Practices and Workplace Safety', 'Clients, Products, and Business Practices', 'Damage to Physical Assets', 'Business Disruption and System Failures', 'Execution, Delivery, and Process Management']
    actual_types = df['Basel_Event_Type'].unique()
    for event_type in actual_types:
      assert event_type in expected_types

def test_generate_synthetic_loss_data_negative():
    with pytest.raises(ValueError):
        generate_synthetic_loss_data(-1)
