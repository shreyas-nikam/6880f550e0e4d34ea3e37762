import pytest
import pandas as pd
from definition_4fcc003968a14be3a322e97ac558caa8 import filter_data

@pytest.fixture
def sample_dataframe():
    data = {'event_type': ['Fraud', 'System Failure', 'Fraud', 'Process Error'],
            'date': pd.to_datetime(['2023-01-01', '2023-02-15', '2023-03-01', '2023-04-10']),
            'loss_amount': [100.0, 200.0, 150.0, 50.0]}
    return pd.DataFrame(data)

def test_filter_data_no_filters(sample_dataframe):
    filtered_df = filter_data(sample_dataframe, None, None, None)
    assert filtered_df.equals(sample_dataframe)

def test_filter_data_event_type(sample_dataframe):
    filtered_df = filter_data(sample_dataframe, ['Fraud'], None, None)
    assert len(filtered_df) == 2
    assert all(filtered_df['event_type'] == 'Fraud')

def test_filter_data_date_range(sample_dataframe):
    start_date = pd.to_datetime('2023-02-01')
    end_date = pd.to_datetime('2023-03-15')
    filtered_df = filter_data(sample_dataframe, None, (start_date, end_date), None)
    assert len(filtered_df) == 2
    assert filtered_df['date'].min() >= start_date
    assert filtered_df['date'].max() <= end_date

def test_filter_data_loss_amount_range(sample_dataframe):
    filtered_df = filter_data(sample_dataframe, None, None, (120.0, 250.0))
    assert len(filtered_df) == 2
    assert filtered_df['loss_amount'].min() >= 120.0
    assert filtered_df['loss_amount'].max() <= 250.0

def test_filter_data_all_filters(sample_dataframe):
    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2023-03-01')
    filtered_df = filter_data(sample_dataframe, ['Fraud'], (start_date, end_date), (90.0, 160.0))
    assert len(filtered_df) == 2
    assert all(filtered_df['event_type'] == 'Fraud')
    assert filtered_df['date'].min() >= start_date
    assert filtered_df['date'].max() <= end_date
    assert filtered_df['loss_amount'].min() >= 90.0
    assert filtered_df['loss_amount'].max() <= 160.0

