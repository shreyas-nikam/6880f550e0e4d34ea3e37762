import pandas as pd
import numpy as np

def generate_synthetic_loss_data(num_records):
    """Creates a pandas.DataFrame representing synthetic operational loss events."""
    if num_records < 0:
        raise ValueError("Number of records must be non-negative.")

    event_ids = [f'Event-{i+1}' for i in range(num_records)]
    dates = pd.to_datetime(np.random.choice(pd.date_range('2020-01-01', '2023-12-31'), num_records))
    basel_event_types = np.random.choice(['Internal Fraud', 'External Fraud', 'Employment Practices and Workplace Safety', 'Clients, Products, and Business Practices', 'Damage to Physical Assets', 'Business Disruption and System Failures', 'Execution, Delivery, and Process Management'], num_records)
    loss_amounts = np.random.uniform(1000, 1000000, num_records)
    impact_categories = np.random.choice(['Financial', 'Reputational', 'Operational', 'Compliance'], num_records)
    contributing_factors = np.random.choice(['Human Error', 'System Failure', 'Process Deficiency', 'External Event'], num_records)

    df = pd.DataFrame({
        'Event_ID': event_ids,
        'Date': dates,
        'Basel_Event_Type': basel_event_types,
        'Loss_Amount': loss_amounts,
        'Impact_Category': impact_categories,
        'Contributing_Factors': contributing_factors
    })

    return df

import pandas as pd

def validate_data(df):
    """Confirms data integrity and readiness for analysis."""
    required_columns = ['Event_ID', 'Date', 'Basel_Event_Type', 'Loss_Amount']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' is missing.")
    if df.empty:
        raise KeyError("DataFrame is empty.")
    if not pd.api.types.is_numeric_dtype(df['Event_ID']):
        raise ValueError("Event_ID must be numeric.")
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        try:
            df['Date'] = pd.to_datetime(df['Date'])
        except:
            raise ValueError("Date must be a valid date.")
    if not pd.api.types.is_string_dtype(df['Basel_Event_Type']):
        raise ValueError("Basel_Event_Type must be a string.")
    if not pd.api.types.is_numeric_dtype(df['Loss_Amount']):
        raise ValueError("Loss_Amount must be numeric.")
    if df.isnull().values.any():
        raise ValueError("DataFrame contains missing values.")
    return None

import pandas as pd

def filter_data(df, event_type, date_range, loss_amount_range):
    """Filters DataFrame based on user selections."""
    filtered_df = df.copy()

    if event_type:
        filtered_df = filtered_df[filtered_df['event_type'].isin(event_type)]

    if date_range:
        start_date, end_date = date_range
        filtered_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]

    if loss_amount_range:
        min_amount, max_amount = loss_amount_range
        filtered_df = filtered_df[(filtered_df['loss_amount'] >= min_amount) & (filtered_df['loss_amount'] <= max_amount)]

    return filtered_df

import pandas as pd

def calculate_summary_statistics(df):
    """Computes key statistical measures for the filtered data."""

    total_loss_amount = df['Loss_Amount'].sum() if not df.empty else 0
    average_loss_amount = df['Loss_Amount'].mean() if not df.empty else 0

    event_count_per_type = df['Basel_Event_Type'].value_counts().to_dict() if not df.empty else {}

    average_loss_amount_per_type = {}
    if not df.empty:
        for event_type in df['Basel_Event_Type'].unique():
            average_loss_amount_per_type[event_type] = df[df['Basel_Event_Type'] == event_type]['Loss_Amount'].mean()

    return {
        'total_loss_amount': total_loss_amount,
        'average_loss_amount': average_loss_amount,
        'event_count_per_type': event_count_per_type,
        'average_loss_amount_per_type': average_loss_amount_per_type
    }

import pandas as pd
import matplotlib.pyplot as plt

def plot_trend(df, title, x_label, y_label):
    """Visualizes loss trends over time.
    Args:
        df (pandas DataFrame): DataFrame with Date, Basel_Event_Type, Loss_Amount.
        title (str): Plot title.
        x_label (str): X-axis label.
        y_label (str): Y-axis label.
    """
    if not isinstance(df, pd.DataFrame):
        raise AttributeError("df must be a pandas DataFrame")

    if df.empty:
        return

    if 'Date' not in df.columns or 'Basel_Event_Type' not in df.columns or 'Loss_Amount' not in df.columns:
        raise KeyError("DataFrame must contain 'Date', 'Basel_Event_Type', and 'Loss_Amount' columns")

    df['Date'] = pd.to_datetime(df['Date'])

    fig, ax = plt.subplots(figsize=(10, 6))

    for event_type in df['Basel_Event_Type'].unique():
        df_event = df[df['Basel_Event_Type'] == event_type]
        ax.plot(df_event['Date'], df_event['Loss_Amount'], label=event_type)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def plot_aggregated_comparison(df, title, x_label, y_label):
    """Compares total loss across categorical dimensions."""
    if df.empty:
        print("DataFrame is empty. No plot to generate.")
        return

    try:
        if 'Basel_Event_Type' not in df.columns or 'Loss_Amount' not in df.columns:
            print("Required columns 'Basel_Event_Type' or 'Loss_Amount' are missing.")
            return
        
        df['Loss_Amount'] = pd.to_numeric(df['Loss_Amount'], errors='coerce')
        df = df.dropna(subset=['Loss_Amount'])
        
        aggregated_data = df.groupby('Basel_Event_Type')['Loss_Amount'].sum()

        if aggregated_data.empty:
            print("No data to plot after processing.")
            return
        
        aggregated_data.plot(kind='bar')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred during plotting: {e}")

import pandas as pd
import matplotlib.pyplot as plt

def plot_relationship(df, title, x_label, y_label):
    """Explores relationship between Loss_Amount and event frequency."""
    if df.empty:
        return

    if not {'Loss_Amount', 'Frequency', 'Impact_Category'}.issubset(df.columns):
        return

    try:
        df['Loss_Amount'] = pd.to_numeric(df['Loss_Amount'])
        df['Frequency'] = pd.to_numeric(df['Frequency'])
    except ValueError:
        raise TypeError("Loss_Amount and Frequency must be numeric")
        

    fig, ax = plt.subplots()
    for category in df['Impact_Category'].unique():
        subset = df[df['Impact_Category'] == category]
        ax.scatter(subset['Frequency'], subset['Loss_Amount'], label=category)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.show()
    plt.close()

import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
import pandas as pd

def create_interactive_filters(df):
    """Sets up and displays ipywidgets for user interaction."""

    if df.empty:
        print("DataFrame is empty. No filters to create.")
        return

    # Unique Basel Event Types
    basel_event_types = sorted(df['Basel_Event_Type'].unique())

    # Date Range Slider
    date_min = df['Date'].min().to_pydatetime()
    date_max = df['Date'].max().to_pydatetime()

    # Loss Amount Range Slider
    loss_amount_min = int(df['Loss_Amount'].min())
    loss_amount_max = int(df['Loss_Amount'].max())
    
    # Widget definitions
    basel_event_type_dropdown = widgets.Dropdown(
        options=['All'] + basel_event_types,
        description='Basel Event Type:',
        disabled=False,
    )

    date_range_slider = widgets.SelectionRangeSlider(
        options=[(date.strftime('%Y-%m-%d'), date) for date in pd.date_range(date_min, date_max)],
        index=(0, len(pd.date_range(date_min, date_max)) - 1),
        description='Date Range:',
        disabled=False
    )

    loss_amount_range_slider = widgets.IntRangeSlider(
        value=[loss_amount_min, loss_amount_max],
        min=loss_amount_min,
        max=loss_amount_max,
        step=1,
        description='Loss Amount Range:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d'
    )

    # Display the widgets.  No interaction is set up.
    display(basel_event_type_dropdown)
    display(date_range_slider)
    display(loss_amount_range_slider)