
import streamlit as st
import pandas as pd
import plotly.express as px

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
        # As per the provided Jupyter Notebook, the 'Weighted' matrix is currently identical to 'Simple'.
        # The handbook suggests this approach could involve different weighting for control ratings.
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

def store_risk_assessment_inputs(unit_name, inherent_risk, controls, control_effectiveness=None, control_attributes=None):
    """Stores risk assessment details in Streamlit session state."""
    # Ensure 'controls' is always a list for consistent storage
    if not isinstance(controls, list):
        controls = [c.strip() for c in controls.split(',')] if controls else []

    # Store with control details, allowing for updates
    if unit_name not in st.session_state.risk_assessment_data:
        st.session_state.risk_assessment_data[unit_name] = {
            "inherent_risk": inherent_risk,
            "controls": {} # Controls will be a dictionary by name for detailed storage
        }

    # Add or update control details
    for control_name in controls:
        st.session_state.risk_assessment_data[unit_name]["controls"][control_name] = {
            "effectiveness": control_effectiveness,
            "attributes": control_attributes if control_attributes is not None else []
        }

    # Update inherent risk if it changes
    st.session_state.risk_assessment_data[unit_name]["inherent_risk"] = inherent_risk

    st.success(f"Risk assessment for '{unit_name}' stored successfully!")
    st.json(st.session_state.risk_assessment_data) # Display current state


def run_risk_assessment():
    st.header("Risk Assessment")

    # Initialize session state variables
    if 'risk_assessment_data' not in st.session_state:
        st.session_state.risk_assessment_data = {}

    st.subheader("Define Risk Assessment Units")
    unit_name = st.text_input("Business Unit Name")
    inherent_risk = st.selectbox("Inherent Risk Level", options=['High', 'Medium', 'Low'])
    controls = st.text_area("Controls (comma-separated)")

    if st.button("Store Risk Assessment"):
        store_risk_assessment_inputs(unit_name, inherent_risk, controls)

    st.subheader("Calculate Residual Risk")
    inherent_risk_input = st.selectbox("Select Inherent Risk Level", options=['High', 'Medium', 'Low'])
    control_effectiveness_input = st.selectbox("Select Control Effectiveness Level", options=['Effective', 'Partially Effective', 'Ineffective'])
    approach_input = st.selectbox("Select Calculation Approach", options=['Simple', 'Weighted'])

    residual_risk = calculate_residual_risk(inherent_risk_input, control_effectiveness_input, approach_input)
    st.markdown(f"### Residual Risk: {residual_risk}")

    # Heatmap Visualization
    st.subheader("Residual Risk Heatmap")
    data = [
        ["Low", "Medium", "High"],
        ["Low", "Medium", "High"],
        ["Low", "Low", "Medium"],
    ]

    if approach_input == "Simple":
        data = [
            ["Low", "Medium", "High"],
            ["Low", "Medium", "High"],
            ["Low", "Low", "Medium"],
        ]
    elif approach_input == "Weighted":
         data = [
            ["Low", "Medium", "High"],
            ["Low", "Medium", "High"],
            ["Low", "Low", "Medium"],
        ]

    df = pd.DataFrame(data, columns=["Ineffective", "Partially Effective", "Effective"], index = ["High", "Medium", "Low"])

    fig = px.imshow(df,
                    labels=dict(x="Control Effectiveness", y="Inherent Risk", color="Residual Risk"),
                    x=df.columns,
                    y=df.index,
                    color_continuous_scale="RdYlGn",
                   )
    st.plotly_chart(fig, use_container_width=True)
