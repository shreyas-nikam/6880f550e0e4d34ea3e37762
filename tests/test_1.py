import pytest
import pandas as pd
from definition_4a0cdca81b5e4fd5af33f4177bf60fcc import validate_data

def test_validate_data_valid():
    data = {'Event_ID': [1, 2], 'Date': ['2023-01-01', '2023-01-02'], 'Basel_Event_Type': ['Fraud', 'Other'], 'Loss_Amount': [100, 200]}
    df = pd.DataFrame(data)
    assert validate_data(df) == None

def test_validate_data_missing_column():
    data = {'Date': ['2023-01-01', '2023-01-02'], 'Basel_Event_Type': ['Fraud', 'Other'], 'Loss_Amount': [100, 200]}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        validate_data(df)

def test_validate_data_incorrect_data_type():
    data = {'Event_ID': [1, 2], 'Date': ['2023-01-01', '2023-01-02'], 'Basel_Event_Type': ['Fraud', 'Other'], 'Loss_Amount': ['a', 'b']}
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        validate_data(df)

def test_validate_data_missing_values():
    data = {'Event_ID': [1, 2], 'Date': ['2023-01-01', None], 'Basel_Event_Type': ['Fraud', 'Other'], 'Loss_Amount': [100, 200]}
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    with pytest.raises(ValueError):
        validate_data(df)

def test_validate_data_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(KeyError):
        validate_data(df)
