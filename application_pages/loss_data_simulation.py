import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

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

        # More realistic loss amount distribution
        loss_amount = np.random.lognormal(mean=8, sigma=1.5)  # Log-normal for realistic loss distribution
        near_miss_flag = np.random.choice([True, False], p=[0.1, 0.9])
        control_breach_type = np.random.choice(["Type1", "Type2", "Type3"])
        recovery_time_days = np.random.randint(1, 30)

        data.append([timestamp, business_unit, risk_category, loss_amount, near_miss_flag, control_breach_type, recovery_time_days])

    df = pd.DataFrame(data, columns=["Timestamp", "Business_Unit", "Risk_Category", "Loss_Amount", "Near_Miss_Flag", "Control_Breach_Type", "Recovery_Time_Days"])
    return df.sort_values('Timestamp')

def run_overview_loss_simulation():    
    # Loss Data Simulation Section
    st.header("Loss Data Simulation")
    
    # Add instructions before the input controls
    st.markdown("""
    ### Simulation Instructions
    
    **Configure Your Simulation:**
    1. **Number of Events**: Choose how many loss events to generate (100-10,000). More events provide better trend visualization.
    2. **Date Range**: Select the time period for your simulation data.
    3. **Business Units**: Select which business units to include in the simulation.
    4. **Risk Categories**: Choose the types of operational risks to simulate.
    5. Click **"Generate Loss Data"** to create your synthetic dataset.
    """)

    # Initialize session state variable
    if 'loss_data' not in st.session_state:
        st.session_state.loss_data = pd.DataFrame()

    # Simulation Parameters
    col1, col2 = st.columns(2)
    
    with col1:
        num_events = st.number_input("Number of Loss Events to Simulate", min_value=100, max_value=10000, value=1000)
        start_date, end_date = st.date_input("Simulation Date Range", value=[pd.to_datetime('2023-01-01'), pd.to_datetime('2023-12-31')])
    
    with col2:
        business_units = st.multiselect("Select Business Units", options=['Investment Banking', 'Retail Banking', 'Asset Management', 'Operations'], default=['Investment Banking', 'Retail Banking'])
        risk_categories = st.multiselect("Select Risk Categories", options=['Internal Fraud', 'External Fraud', 'System Failures', 'Process Errors'], default=['Internal Fraud', 'System Failures'])

    if st.button("Generate Loss Data", type="primary"):
        with st.spinner("Generating synthetic loss data..."):
            st.session_state.loss_data = generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)
        st.success(f"Successfully generated {len(st.session_state.loss_data)} loss events!")

    if not st.session_state.loss_data.empty:
        st.subheader("Generated Loss Data Overview")
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Events", len(st.session_state.loss_data))
        with col2:
            st.metric("Total Loss Amount", f"${st.session_state.loss_data['Loss_Amount'].sum():,.0f}")
        with col3:
            st.metric("Average Loss", f"${st.session_state.loss_data['Loss_Amount'].mean():,.0f}")
        with col4:
            st.metric("Max Loss", f"${st.session_state.loss_data['Loss_Amount'].max():,.0f}")
        
        # Data preview
        with st.expander("View Raw Data Sample"):
            st.dataframe(st.session_state.loss_data.head(10))

        st.subheader("Loss Data Visualizations")

        # Improved Trend Plot - Monthly Aggregation
        st.markdown("### Monthly Loss Trend")
        
        # Aggregate by month for cleaner visualization
        monthly_data = st.session_state.loss_data.copy()
        monthly_data['Year_Month'] = monthly_data['Timestamp'].dt.to_period('M')
        monthly_agg = monthly_data.groupby('Year_Month').agg({
            'Loss_Amount': ['sum', 'mean', 'count']
        }).round(2)
        monthly_agg.columns = ['Total_Loss', 'Average_Loss', 'Event_Count']
        monthly_agg = monthly_agg.reset_index()
        monthly_agg['Year_Month'] = monthly_agg['Year_Month'].dt.to_timestamp()
        
        # Create subplot with dual y-axis
        fig_trend = go.Figure()
        
        # Add total loss amount
        fig_trend.add_trace(go.Scatter(
            x=monthly_agg['Year_Month'], 
            y=monthly_agg['Total_Loss'],
            mode='lines+markers',
            name='Total Monthly Loss',
            line=dict(color='red', width=3),
            marker=dict(size=8)
        ))
        
        fig_trend.update_layout(
            title="Monthly Operational Loss Trends",
            xaxis_title="Month",
            yaxis_title="Loss Amount ($)",
            hovermode='x unified',
            showlegend=True,
            height=500
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)

        # Event count trend
        st.markdown("### Monthly Event Count")
        fig_count = px.bar(monthly_agg, x='Year_Month', y='Event_Count', 
                          title="Number of Loss Events per Month",
                          labels={'Event_Count': 'Number of Events', 'Year_Month': 'Month'})
        fig_count.update_layout(height=400)
        st.plotly_chart(fig_count, use_container_width=True)

        # Loss distribution
        st.markdown("### Loss Amount Distribution")
        fig_hist = px.histogram(st.session_state.loss_data, x="Loss_Amount", nbins=50,
                               title="Distribution of Loss Amounts",
                               labels={'Loss_Amount': 'Loss Amount ($)', 'count': 'Frequency'})
        fig_hist.update_layout(height=400)
        st.plotly_chart(fig_hist, use_container_width=True)

        # Business unit comparison
        st.markdown("### Loss Analysis by Business Unit")
        col1, col2 = st.columns(2)
        
        with col1:
            # Total loss by business unit
            loss_by_bu = st.session_state.loss_data.groupby("Business_Unit")["Loss_Amount"].sum().reset_index()
            fig_bar = px.bar(loss_by_bu, x="Business_Unit", y="Loss_Amount", 
                            title="Total Loss Amount by Business Unit",
                            color="Loss_Amount", color_continuous_scale="Reds")
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            # Average loss by business unit
            avg_loss_by_bu = st.session_state.loss_data.groupby("Business_Unit")["Loss_Amount"].mean().reset_index()
            fig_avg = px.bar(avg_loss_by_bu, x="Business_Unit", y="Loss_Amount", 
                            title="Average Loss Amount by Business Unit",
                            color="Loss_Amount", color_continuous_scale="Blues")
            st.plotly_chart(fig_avg, use_container_width=True)

        # Risk category analysis
        st.markdown("### Loss Analysis by Risk Category")
        loss_by_risk = st.session_state.loss_data.groupby("Risk_Category").agg({
            'Loss_Amount': ['sum', 'mean', 'count']
        }).round(2)
        loss_by_risk.columns = ['Total_Loss', 'Average_Loss', 'Event_Count']
        loss_by_risk = loss_by_risk.reset_index()
        
        fig_sunburst = px.sunburst(st.session_state.loss_data, 
                                  path=['Risk_Category', 'Business_Unit'], 
                                  values='Loss_Amount',
                                  title="Loss Distribution by Risk Category and Business Unit")
        st.plotly_chart(fig_sunburst, use_container_width=True)

        # Recovery time analysis
        st.markdown("### Recovery Time vs Loss Severity")
        fig_scatter = px.scatter(st.session_state.loss_data, x="Recovery_Time_Days", y="Loss_Amount", 
                               color="Business_Unit", size="Loss_Amount",
                               title="Loss Amount vs. Recovery Time",
                               labels={'Recovery_Time_Days': 'Recovery Time (Days)', 'Loss_Amount': 'Loss Amount ($)'},
                               hover_data=['Risk_Category'])
        fig_scatter.update_layout(height=500)
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Summary insights
        st.markdown("### Key Insights")
        total_loss = st.session_state.loss_data['Loss_Amount'].sum()
        avg_recovery = st.session_state.loss_data['Recovery_Time_Days'].mean()
        highest_risk_bu = loss_by_bu.loc[loss_by_bu['Loss_Amount'].idxmax(), 'Business_Unit']
        
        st.info(f"""
        **Risk Profile Summary:**
        - **Highest Risk Business Unit:** {highest_risk_bu}
        - **Average Recovery Time:** {avg_recovery:.1f} days
        - **Total Simulated Losses:** ${total_loss:,.0f}
        - **Risk Concentration:** {(loss_by_bu['Loss_Amount'].max() / total_loss * 100):.1f}% of losses from top business unit
        """)
