
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories):
    """Generates a synthetic dataset of operational loss events."""
    data = []
    for _ in range(num_events):
        timestamp = pd.to_datetime(start_date) + pd.to_timedelta(np.random.randint(0, (end_date - start_date).days + 1), unit='D')

        # Handle empty lists for business units and risk categories
        if business_units:
            business_unit = np.random.choice(business_units)
        else:
            business_unit = np.random.choice(["BU1", "BU2", "BU3"])  #Default values
        if risk_categories:
            risk_category = np.random.choice(risk_categories)
        else:
            risk_category = np.random.choice(["RC1", "RC2", "RC3"])  #Default values

        loss_amount = np.random.normal(10000, 5000)
        near_miss_flag = np.random.choice([True, False], p=[0.1, 0.9])
        control_breach_type = np.random.choice(["Type1", "Type2", "Type3"])
        recovery_time_days = np.random.randint(1, 30)

        data.append([timestamp, business_unit, risk_category, loss_amount, near_miss_flag, control_breach_type, recovery_time_days])

    df = pd.DataFrame(data, columns=["Timestamp", "Business_Unit", "Risk_Category", "Loss_Amount", "Near_Miss_Flag", "Control_Breach_Type", "Recovery_Time_Days"])
    return df

def run_loss_data_simulation():
    st.header("Loss Data Simulation")

    # Initialize session state variable
    if 'loss_data' not in st.session_state:
        st.session_state.loss_data = pd.DataFrame() # Initialize as empty DataFrame

    num_events = st.number_input("Number of Loss Events to Simulate", min_value=100, max_value=10000, value=1000)
    start_date, end_date = st.date_input("Simulation Date Range", value=[pd.to_datetime('2023-01-01'), pd.to_datetime('2023-12-31')])
    business_units = st.multiselect("Select Business Units (optional)", options=['BU1', 'BU2', 'BU3', 'BU4'], default=['BU1', 'BU2', 'BU3'])
    risk_categories = st.multiselect("Select Risk Categories (optional)", options=['RC1', 'RC2', 'RC3', 'RC4'], default=['RC1', 'RC2'])

    if st.button("Generate Loss Data"):
        st.session_state.loss_data = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)
        st.success("Loss data generated successfully!")

    if not st.session_state.loss_data.empty:
        st.subheader("Generated Loss Data (Preview)")
        st.dataframe(st.session_state.loss_data.head())

        st.subheader("Loss Data Visualizations")

        # Trend Plot
        st.markdown("### Loss Amount Trend")
        fig_trend = px.line(st.session_state.loss_data, x="Timestamp", y="Loss_Amount", title="Loss Amount Over Time")
        st.plotly_chart(fig_trend, use_container_width=True)

        # Relationship Plot
        st.markdown("### Loss Amount vs. Recovery Time")
        fig_scatter = px.scatter(st.session_state.loss_data, x="Recovery_Time_Days", y="Loss_Amount", title="Loss Amount vs. Recovery Time (Days)")
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Aggregated Comparison
        st.markdown("### Total Loss Amount by Business Unit")
        loss_by_bu = st.session_state.loss_data.groupby("Business_Unit")["Loss_Amount"].sum().reset_index()
        fig_bar = px.bar(loss_by_bu, x="Business_Unit", y="Loss_Amount", title="Total Loss Amount by Business Unit")
        st.plotly_chart(fig_bar, use_container_width=True)
