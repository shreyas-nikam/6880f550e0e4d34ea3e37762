import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories):
    """Creates a synthetic dataset of operational loss events."""
    
    start = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
    end = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
    
    data = []
    for _ in range(num_events):
        timestamp = start + timedelta(seconds=np.random.randint(0, int((end - start).total_seconds())))
        
        if business_units:
            business_unit = np.random.choice(business_units)
        else:
            business_unit = None
            
        if risk_categories:
            risk_category = np.random.choice(risk_categories)
        else:
            risk_category = None
            
        loss_amount = np.random.randint(100, 10000)
        near_miss_flag = np.random.choice([True, False])
        control_breach_type = np.random.choice(["Type1", "Type2", "Type3", None])
        recovery_time_days = np.random.randint(1, 30)
        
        data.append([timestamp, business_unit, risk_category, loss_amount, near_miss_flag, control_breach_type, recovery_time_days])
        
    df = pd.DataFrame(data, columns=["Timestamp", "Business_Unit", "Risk_Category", "Loss_Amount", "Near_Miss_Flag", "Control_Breach_Type", "Recovery_Time_Days"])
    
    return df

def calculate_residual_risk(inherent_risk_level, control_effectiveness_level, approach):
                """Calculates residual risk based on inherent risk and control effectiveness."""

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
                    raise ValueError("Invalid approach specified.")

                return risk_matrix[(inherent_risk_level, control_effectiveness_level)]

import pandas as pd

data_store = []
def store_risk_assessment_inputs(unit_name, inherent_risk, controls):
    """Stores user-defined risk assessment details."""
    global data_store

    if not isinstance(unit_name, str):
        raise TypeError("Unit name must be a string.")
    if not isinstance(inherent_risk, str):
        raise TypeError("Inherent risk must be a string.")
    if not isinstance(controls, list):
        raise TypeError("Controls must be a list.")
    
    for control in controls:
        if not isinstance(control, dict):
             raise TypeError("Each control must be a dictionary")

    data_store.append({"unit_name": unit_name, "inherent_risk": inherent_risk, "controls": controls})

import pandas as pd

def validate_dataframe(df, expected_columns, expected_dtypes, critical_columns):
    """Checks DataFrame for expected columns, dtypes, and missing values."""
    try:
        if df.empty:
            return True

        for col in expected_columns:
            if col not in df.columns:
                return False
            
            expected_dtype = expected_columns[col]
            actual_dtype = df[col].dtype

            # Simple type check: compare string representation of types
            if expected_dtype == int and actual_dtype != 'int64':
                return False
            if expected_dtype == float and actual_dtype != 'float64':
                return False
            if expected_dtype == str and actual_dtype != 'object':
                return False

        for col in critical_columns:
            if df[col].isnull().any():
                return False

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False