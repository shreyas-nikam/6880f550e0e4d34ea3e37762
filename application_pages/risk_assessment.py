import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
        # Enhanced weighted approach with more nuanced risk calculations
        risk_matrix = {
            ("High", "Effective"): "Low",
            ("High", "Partially Effective"): "Medium-High",
            ("High", "Ineffective"): "High",
            ("Medium", "Effective"): "Very Low",
            ("Medium", "Partially Effective"): "Medium",
            ("Medium", "Ineffective"): "Medium-High",
            ("Low", "Effective"): "Very Low",
            ("Low", "Partially Effective"): "Low",
            ("Low", "Ineffective"): "Medium",
        }
    else:
        raise ValueError("Invalid approach. Must be 'Simple' or 'Weighted'.")
    return risk_matrix[(inherent_risk_level, control_effectiveness_level)]

def store_risk_assessment_inputs(unit_name, inherent_risk, controls, control_effectiveness, risk_description):
    """Stores risk assessment details in Streamlit session state."""
    if 'risk_assessments' not in st.session_state:
        st.session_state.risk_assessments = []
    
    # Calculate residual risk
    residual_risk = calculate_residual_risk(inherent_risk, control_effectiveness, "Simple")
    
    # Store assessment
    assessment = {
        "unit_name": unit_name,
        "inherent_risk": inherent_risk,
        "controls": controls,
        "control_effectiveness": control_effectiveness,
        "residual_risk": residual_risk,
        "risk_description": risk_description
    }
    
    # Check if unit already exists and update, otherwise add new
    existing_index = None
    for i, existing in enumerate(st.session_state.risk_assessments):
        if existing["unit_name"] == unit_name:
            existing_index = i
            break
    
    if existing_index is not None:
        st.session_state.risk_assessments[existing_index] = assessment
        st.success(f"Updated risk assessment for '{unit_name}'!")
    else:
        st.session_state.risk_assessments.append(assessment)
        st.success(f"Added new risk assessment for '{unit_name}'!")

def run_risk_assessment():
    st.header("Risk Assessment & Management")

    # Enhanced Overview Section
    st.markdown("""
    ## Risk Assessment Instructions

    This page allows you to perform comprehensive operational risk assessments for different business units. Follow the steps below to conduct your assessment:

    ### How to Use This Tool
    
    **Step 1: Define Business Units**
    - Enter a meaningful business unit name (e.g., "Trading Desk", "Loan Processing", "IT Operations")
    - Describe the key risk you're assessing for this unit
    - Select the inherent risk level based on the unit's exposure
    
    **Step 2: Assess Controls**
    - List the controls in place (e.g., "Dual authorization, System monitoring, Daily reconciliation")
    - Evaluate how effective these controls are in mitigating the risk
    
    **Step 3: Review Results**
    - View the calculated residual risk
    - Analyze the risk portfolio across all business units
    - Use the heatmap to understand risk patterns

    ### Risk Level Definitions

    **Inherent Risk Levels:**
    - **High**: Significant potential for major operational losses (> $1M)
    - **Medium**: Moderate potential for operational losses ($100K - $1M)
    - **Low**: Limited potential for operational losses (< $100K)
    
    **Control Effectiveness:**
    - **Effective**: Controls consistently prevent/detect issues (>90% effectiveness)
    - **Partially Effective**: Controls sometimes fail (60-90% effectiveness)
    - **Ineffective**: Controls frequently fail or don't exist (<60% effectiveness)
    """)
    
    st.divider()

    # Initialize session state variables
    if 'risk_assessments' not in st.session_state:
        st.session_state.risk_assessments = []

    # Input Section
    st.subheader("Define Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        unit_name = st.text_input(
            "Business Unit Name", 
            placeholder="e.g., Trading Operations, Loan Processing, IT Support",
            help="Enter a descriptive name for the business unit you're assessing"
        )
        
        inherent_risk = st.selectbox(
            "Inherent Risk Level", 
            options=['High', 'Medium', 'Low'],
            help="Select the risk level before considering any controls"
        )
        
        risk_description = st.text_area(
            "Risk Description",
            placeholder="e.g., Risk of trading errors due to manual processes and high transaction volumes",
            help="Describe the specific operational risk you're assessing"
        )
    
    with col2:
        controls = st.text_area(
            "Controls in Place", 
            placeholder="e.g., Dual authorization, Real-time monitoring, Daily reconciliation, Supervisor review",
            help="List the controls that mitigate this risk (comma-separated)"
        )
        
        control_effectiveness = st.selectbox(
            "Control Effectiveness Level", 
            options=['Effective', 'Partially Effective', 'Ineffective'],
            help="Assess how well the controls actually work in practice"
        )

    # Add assessment button
    if st.button("Add/Update Risk Assessment", type="primary"):
        if unit_name and risk_description and controls:
            store_risk_assessment_inputs(unit_name, inherent_risk, controls, control_effectiveness, risk_description)
        else:
            st.error("❌ Please fill in all required fields (Business Unit Name, Risk Description, and Controls)")

    st.divider()

    # Display existing assessments
    if st.session_state.risk_assessments:
        st.subheader("Risk Assessment Portfolio")
        
        # Create DataFrame for analysis
        df_assessments = pd.DataFrame(st.session_state.risk_assessments)
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Assessments", len(df_assessments))
        with col2:
            high_risk_count = len(df_assessments[df_assessments['residual_risk'].isin(['High', 'Medium-High'])])
            st.metric("High Risk Units", high_risk_count)
        with col3:
            effective_controls = len(df_assessments[df_assessments['control_effectiveness'] == 'Effective'])
            st.metric("Units with Effective Controls", effective_controls)
        with col4:
            risk_reduction = len(df_assessments[df_assessments['inherent_risk'] != df_assessments['residual_risk']])
            st.metric("Risk Reduction Cases", risk_reduction)

        # Detailed assessments table
        st.markdown("### Assessment Details")
        
        # Format the data for better display
        display_df = df_assessments.copy()
        display_df = display_df[['unit_name', 'inherent_risk', 'control_effectiveness', 'residual_risk', 'risk_description']]
        display_df.columns = ['Business Unit', 'Inherent Risk', 'Control Effectiveness', 'Residual Risk', 'Risk Description']
        
        st.dataframe(display_df, use_container_width=True)
        
        # Visualizations
        st.markdown("### Risk Analysis Visualizations")
        
        # Risk distribution charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Inherent vs Residual Risk comparison
            risk_comparison = pd.DataFrame({
                'Risk Type': ['Inherent Risk'] * len(df_assessments) + ['Residual Risk'] * len(df_assessments),
                'Risk Level': list(df_assessments['inherent_risk']) + list(df_assessments['residual_risk']),
                'Business Unit': list(df_assessments['unit_name']) + list(df_assessments['unit_name'])
            })
            
            fig_comparison = px.histogram(
                risk_comparison, 
                x='Risk Level', 
                color='Risk Type',
                barmode='group',
                title="Inherent vs Residual Risk Distribution",
                category_orders={'Risk Level': ['Low', 'Medium', 'Medium-High', 'High']}
            )
            st.plotly_chart(fig_comparison, use_container_width=True)
        
        with col2:
            # Control effectiveness distribution
            fig_controls = px.pie(
                df_assessments, 
                names='control_effectiveness',
                title="Control Effectiveness Distribution",
                color_discrete_map={
                    'Effective': '#2E8B57',
                    'Partially Effective': '#FFD700', 
                    'Ineffective': '#DC143C'
                }
            )
            st.plotly_chart(fig_controls, use_container_width=True)

        # Risk matrix visualization
        st.markdown("### Risk Heat Map")
        
        # Create risk matrix data
        risk_levels = ['Low', 'Medium', 'High']
        control_levels = ['Ineffective', 'Partially Effective', 'Effective']
        
        # Simple approach matrix
        matrix_data = []
        matrix_colors = []
        for inherent in risk_levels:
            row_data = []
            row_colors = []
            for control in control_levels:
                residual = calculate_residual_risk(inherent, control, "Simple")
                row_data.append(residual)
                # Color mapping
                color_map = {'Low': 1, 'Medium': 2, 'Medium-High': 3, 'High': 4, 'Very Low': 0}
                row_colors.append(color_map.get(residual, 2))
            matrix_data.append(row_data)
            matrix_colors.append(row_colors)

        fig_heatmap = go.Figure(data=go.Heatmap(
            z=matrix_colors,
            x=control_levels,
            y=risk_levels[::-1],  # Reverse to show High at top
            text=matrix_data[::-1],  # Reverse to match y-axis
            texttemplate="%{text}",
            textfont={"size": 12, "color": "white"},
            colorscale=[[0, '#90EE90'], [0.25, '#FFFF00'], [0.5, '#FFA500'], [0.75, '#FF6347'], [1, '#DC143C']],
            showscale=False,
            hoverongaps=False
        ))
        
        fig_heatmap.update_layout(
            title="Risk Assessment Matrix (Inherent Risk vs Control Effectiveness)",
            xaxis_title="Control Effectiveness",
            yaxis_title="Inherent Risk Level",
            height=400
        )
        
        st.plotly_chart(fig_heatmap, use_container_width=True)

        # Business unit risk profile
        st.markdown("### Business Unit Risk Profiles")
        
        # Create a comprehensive view
        fig_profile = px.scatter(
            df_assessments,
            x='inherent_risk',
            y='control_effectiveness',
            size=[10] * len(df_assessments),  # Fixed size for visibility
            color='residual_risk',
            hover_name='unit_name',
            hover_data=['risk_description'],
            title="Risk Profile by Business Unit",
            color_discrete_map={
                'Low': '#2E8B57',
                'Medium': '#FFD700',
                'Medium-High': '#FF6347',
                'High': '#DC143C',
                'Very Low': '#90EE90'
            }
        )
        
        fig_profile.update_layout(height=500)
        st.plotly_chart(fig_profile, use_container_width=True)

        # Risk improvement recommendations
        st.markdown("### Risk Management Recommendations")
        
        high_risk_units = df_assessments[df_assessments['residual_risk'].isin(['High', 'Medium-High'])]
        ineffective_controls = df_assessments[df_assessments['control_effectiveness'] == 'Ineffective']
        
        if len(high_risk_units) > 0:
            st.warning(f"**High Priority Actions Required:**")
            for _, unit in high_risk_units.iterrows():
                st.write(f"- **{unit['unit_name']}**: Residual risk is {unit['residual_risk']}. Consider strengthening controls.")
        
        if len(ineffective_controls) > 0:
            st.error(f"**Control Effectiveness Issues:**")
            for _, unit in ineffective_controls.iterrows():
                st.write(f"- **{unit['unit_name']}**: Controls are ineffective. Immediate review required.")
        
        if len(high_risk_units) == 0 and len(ineffective_controls) == 0:
            st.success("**Good Risk Posture**: All business units have acceptable residual risk levels with effective controls.")

    else:
        st.info("**Get Started**: Add your first risk assessment using the form above to see visualizations and analysis.")

    # Educational content
    with st.expander("Learn More About Risk Assessment"):
        st.markdown("""
        ### Risk Assessment Best Practices
        
        **1. Inherent Risk Assessment:**
        - Consider the risk without any controls in place
        - Think about potential impact and likelihood
        - Factor in business complexity and external environment
        
        **2. Control Evaluation:**
        - Assess both design and operating effectiveness
        - Consider preventive vs. detective controls
        - Review control testing results and monitoring data
        
        **3. Residual Risk Calculation:**
        - Residual Risk = Inherent Risk - Control Effectiveness
        - Regular reassessment is crucial as risks evolve
        - Document assumptions and rationale
        
        **4. Risk Treatment Options:**
        - **Accept**: For low residual risks within appetite
        - **Mitigate**: Strengthen controls for medium risks
        - **Transfer**: Consider insurance or outsourcing
        - **Avoid**: Eliminate high-risk activities if possible
        """)
