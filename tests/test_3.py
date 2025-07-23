import pytest
import pandas as pd
from definition_78e0164bbe094b928f7259bae6cfe624 import validate_dataframe

@pytest.fixture
def sample_dataframe():
    data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [1.1, 2.2, 3.3]}
    return pd.DataFrame(data)

def test_valid_dataframe(sample_dataframe):
    expected_columns = {'col1': int, 'col2': str, 'col3': float}
    expected_dtypes = {'col1': int, 'col2': object, 'col3': float}
    critical_columns = ['col1', 'col2', 'col3']
    assert validate_dataframe(sample_dataframe, expected_columns, expected_dtypes, critical_columns) == True

def test_missing_critical_value(sample_dataframe):
    sample_dataframe.loc[0, 'col1'] = None
    expected_columns = {'col1': int, 'col2': str, 'col3': float}
    expected_dtypes = {'col1': int, 'col2': object, 'col3': float}
    critical_columns = ['col1']
    assert validate_dataframe(sample_dataframe, expected_columns, expected_dtypes, critical_columns) == False

def test_incorrect_column_name(sample_dataframe):
    expected_columns = {'col_typo': int, 'col2': str, 'col3': float}
    expected_dtypes = {'col_typo': int, 'col2': object, 'col3': float}
    critical_columns = ['col_typo']
    assert validate_dataframe(sample_dataframe, expected_columns, expected_dtypes, critical_columns) == False

def test_incorrect_data_type(sample_dataframe):
    expected_columns = {'col1': int, 'col2': str, 'col3': int}
    expected_dtypes = {'col1': int, 'col2': object, 'col3': int}
    critical_columns = ['col3']
    assert validate_dataframe(sample_dataframe, expected_columns, expected_dtypes, critical_columns) == False

def test_empty_dataframe():
    df = pd.DataFrame()
    expected_columns = {'col1': int}
    expected_dtypes = {'col1': int}
    critical_columns = ['col1']
    assert validate_dataframe(df, expected_columns, expected_dtypes, critical_columns) == False
