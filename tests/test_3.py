import pytest
import pandas as pd
from definition_3d947d62d83f42ef808e9d90adfb0501 import calculate_summary_statistics

def create_sample_df(data):
    return pd.DataFrame(data)

@pytest.fixture
def sample_dataframe():
    data = {'Loss_Amount': [100, 200, 300, 400, 500],
            'Basel_Event_Type': ['Fraud', 'Fraud', 'System Failure', 'Fraud', 'System Failure']}
    return create_sample_df(data)

def test_calculate_summary_statistics_basic(sample_dataframe):
    result = calculate_summary_statistics(sample_dataframe)
    assert isinstance(result, dict)
    assert 'total_loss_amount' in result
    assert 'average_loss_amount' in result
    assert 'event_count_per_type' in result
    assert 'average_loss_amount_per_type' in result
    assert result['total_loss_amount'] == 1500
    assert result['average_loss_amount'] == 300
    assert result['event_count_per_type']['Fraud'] == 3
    assert result['event_count_per_type']['System Failure'] == 2
    assert result['average_loss_amount_per_type']['Fraud'] == 266.6666666666667
    assert result['average_loss_amount_per_type']['System Failure'] == 450

def test_calculate_summary_statistics_empty_df():
    empty_df = pd.DataFrame()
    result = calculate_summary_statistics(empty_df)
    assert isinstance(result, dict)
    assert result['total_loss_amount'] == 0
    assert result['average_loss_amount'] == 0
    assert len(result['event_count_per_type']) == 0
    assert len(result['average_loss_amount_per_type']) == 0

def test_calculate_summary_statistics_single_event_type(sample_dataframe):
    single_type_df = sample_dataframe[sample_dataframe['Basel_Event_Type'] == 'Fraud']
    result = calculate_summary_statistics(single_type_df)
    assert result['event_count_per_type']['Fraud'] == 3
    assert 'System Failure' not in result['event_count_per_type']
    assert result['average_loss_amount_per_type']['Fraud'] == 266.6666666666667
    assert 'System Failure' not in result['average_loss_amount_per_type']

def test_calculate_summary_statistics_missing_loss_amount():
        data = {'Loss_Amount': [100, 200, None, 400, 500],
                'Basel_Event_Type': ['Fraud', 'Fraud', 'System Failure', 'Fraud', 'System Failure']}
        df = create_sample_df(data)
        with pytest.raises(TypeError):
           calculate_summary_statistics(df)
           
def test_calculate_summary_statistics_non_numeric_loss_amount():
        data = {'Loss_Amount': [100, 200, "abc", 400, 500],
                'Basel_Event_Type': ['Fraud', 'Fraud', 'System Failure', 'Fraud', 'System Failure']}
        df = create_sample_df(data)
        with pytest.raises(TypeError):
           calculate_summary_statistics(df)

