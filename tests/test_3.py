import pytest
import pandas as pd
from definition_98552583202840f6b9137aa97189199f import validate_dataframe

@pytest.fixture
def sample_dataframe():
    data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [1.1, 2.2, 3.3]}
    return pd.DataFrame(data)

def test_validate_dataframe_valid(sample_dataframe):
    expected_columns = {'col1': int, 'col2': str, 'col3': float}
    critical_columns = ['col1', 'col2']
    assert validate_dataframe(sample_dataframe, expected_columns, None, critical_columns) == True

def test_validate_dataframe_invalid_column(sample_dataframe):
    expected_columns = {'col1': int, 'col4': str, 'col3': float}
    critical_columns = ['col1', 'col4']
    assert validate_dataframe(sample_dataframe, expected_columns, None, critical_columns) == False

def test_validate_dataframe_invalid_dtype(sample_dataframe):
    expected_columns = {'col1': str, 'col2': str, 'col3': float}
    critical_columns = ['col1', 'col2']
    assert validate_dataframe(sample_dataframe, expected_columns, None, critical_columns) == False

def test_validate_dataframe_missing_critical_value(sample_dataframe):
    sample_dataframe.loc[0, 'col1'] = None
    expected_columns = {'col1': int, 'col2': str, 'col3': float}
    critical_columns = ['col1', 'col2']
    assert validate_dataframe(sample_dataframe, expected_columns, None, critical_columns) == False

def test_validate_dataframe_empty_dataframe():
    df = pd.DataFrame()
    expected_columns = {'col1': int, 'col2': str, 'col3': float}
    critical_columns = ['col1', 'col2']
    assert validate_dataframe(df, expected_columns, None, critical_columns) == True
