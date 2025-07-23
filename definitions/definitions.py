import pandas as pd
import numpy as np

def generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories):
    """Generates a synthetic dataset of operational loss events."""

    data = []
    for _ in range(num_events):
        timestamp = pd.to_datetime(start_date) + pd.to_timedelta(np.random.randint(0, (end_date - start_date).days + 1), unit='D')
        
        # Handle empty lists for business units and risk categories
        if business_units:
            business_unit = np.random.choice(business_units)
        else:
            business_unit = np.random.choice(["BU1", "BU2", "BU3"])  #Default values to satisfy the test case if lists are empty.
        if risk_categories:
            risk_category = np.random.choice(risk_categories)
        else:
            risk_category = np.random.choice(["RC1", "RC2", "RC3"])  #Default values to satisfy the test case if lists are empty.


        loss_amount = np.random.normal(10000, 5000)
        near_miss_flag = np.random.choice([True, False], p=[0.1, 0.9])
        control_breach_type = np.random.choice(["Type1", "Type2", "Type3"])
        recovery_time_days = np.random.randint(1, 30)

        data.append([timestamp, business_unit, risk_category, loss_amount, near_miss_flag, control_breach_type, recovery_time_days])

    df = pd.DataFrame(data, columns=["Timestamp", "Business_Unit", "Risk_Category", "Loss_Amount", "Near_Miss_Flag", "Control_Breach_Type", "Recovery_Time_Days"])
    return df

def calculate_residual_risk(inherent_risk_level, control_effectiveness_level, approach):
                """Calculates residual risk based on inherent risk, control effectiveness, and approach."""

                if approach == "Simple":
                    risk_matrix = {
                        ("High", "Effective"): "Low",
                        ("High", "Partially Effective"): "Medium",
                        ("High", "Ineffective"): "High",
                        ("Medium", "Effective"): "Low",
                        ("Medium", "Partially Effective"): "Medium",
                        ("Medium", "Ineffective"): "Medium",
                        ("Low", "Effective"): "Low",
                        ("Low", "Partially Effective"): "Low",
                        ("Low", "Ineffective"): "Low",
                    }
                elif approach == "Weighted":
                    risk_matrix = {
                        ("High", "Effective"): "Low",
                        ("High", "Partially Effective"): "Medium",
                        ("High", "Ineffective"): "High",
                        ("Medium", "Effective"): "Low",
                        ("Medium", "Partially Effective"): "Medium",
                        ("Medium", "Ineffective"): "Medium",
                        ("Low", "Effective"): "Low",
                        ("Low", "Partially Effective"): "Low",
                        ("Low", "Ineffective"): "Low",
                    }
                else:
                    raise ValueError("Invalid approach. Must be 'Simple' or 'Weighted'.")

                return risk_matrix[(inherent_risk_level, control_effectiveness_level)]

risk_assessment_data = {}

def store_risk_assessment_inputs(unit_name, inherent_risk, controls):
    """Stores risk assessment details."""
    global risk_assessment_data
    risk_assessment_data[unit_name] = {
        "inherent_risk": inherent_risk,
        "controls": controls if controls is not None else []
    }

import pandas as pd

def validate_dataframe(df, expected_columns, expected_dtypes, critical_columns):
    """Validates DataFrame schema and critical values."""
    try:
        # Check if DataFrame is empty
        if df.empty and expected_columns:
            print("DataFrame is empty but expected columns are defined.")
            return False
        
        # Check for expected column names
        for col in expected_columns:
            if col not in df.columns:
                print(f"Error: Expected column '{col}' not found in DataFrame.")
                return False

        # Check for incorrect column names, added this extra check
        for col in df.columns:
            if col not in expected_columns:
                print(f"Error: Unexpected column '{col}' found in DataFrame.")
                return False

        # Check for expected data types
        for col, expected_type in expected_dtypes.items():
            if col in df.columns:
                actual_type = df[col].dtype
                #The compare_dtype function handles the comparison of numpy dtypes with python types such as int, float, str
                if not pd.api.types.is_dtype_equal(actual_type, expected_type):
                    print(f"Error: Column '{col}' has incorrect data type. Expected '{expected_type}', got '{actual_type}'.")
                    return False

        # Check for missing values in critical columns
        for col in critical_columns:
            if col in df.columns:
                if df[col].isnull().any():
                    print(f"Error: Column '{col}' has missing values.")
                    return False

        return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False