
# Streamlit Application Requirements Specification: Operational Risk Assessment Lifecycle Simulator

This document outlines the requirements for developing a Streamlit application based on the provided Jupyter Notebook content and user requirements. It will serve as a blueprint, detailing interactive components and integrating relevant code snippets.

## 1. Application Overview

**Purpose and Objectives:**
The primary purpose of this Streamlit application is to provide an interactive simulation of the operational risk assessment lifecycle within a financial institution, as described in the "PRMIA Operational Risk Manager Handbook" [1]. The application aims to educate risk management students, junior risk professionals, and business unit managers by offering a practical, hands-on understanding of how risks are identified, assessed, controlled, and monitored in an iterative process.

**Key Learning Outcomes:**
*   Understand the key stages and flow of a robust operational risk assessment program.
*   Learn how top-down risk identification informs bottom-up control assessment.
*   Explore the interplay between inherent risk, control effectiveness, and residual risk.
*   Recognize the importance of clear taxonomies and consistent tracking in risk management.

**Core Features:**
*   **Interactive Lifecycle Flow**: Guide users through the stages of the risk assessment lifecycle (e.g., Define Risk Assessment Units, Top-down Workshops, Control Assessment, Residual Risk, Management Validation).
*   **Risk Identification Inputs**: Allow users to define inherent risks (e.g., Internal Fraud, System Failure) and assign qualitative levels (High, Medium, Low) for different business units.
*   **Control Assessment Inputs**: Enable users to define controls for identified risks and assess their effectiveness (Effective, Partially Effective, Ineffective), including control attributes (e.g., Preventative/Detective, Key/Non-Key, Manual/Automated).
*   **Residual Risk Calculation & Visualization**: Calculate and visualize residual risk based on user inputs for inherent risk and control effectiveness, leveraging the formula:
    $$R_{risk} = f(I_{risk}, C_{eff})$$
    where $R_{risk}$ is the Residual Risk, $I_{risk}$ is the Inherent Risk, and $C_{eff}$ is the Control Effectiveness. This will include interactive heatmaps.
*   **Issue Management Tracking**: A simple component to track identified issues and action plans for ineffective controls.
*   **Dynamic Data Simulation**: Generate synthetic data for loss events and near misses to populate scenario examples for visualizations.

**Scope & Constraints:**
*   The application must execute end-to-end on a mid-spec laptop (8 GB RAM) in fewer than 5 minutes.
*   Only open-source Python libraries from PyPI may be used (e.g., pandas, numpy, streamlit, plotly).
*   All major steps will include narrative descriptions and explanations.
*   The application must provide an optional lightweight sample dataset if the user omits data upload.

## 2. User Interface Requirements

**Layout and Navigation Structure:**
*   The application will feature a clear, intuitive multi-page or tab-based layout using `st.sidebar` for navigation or `st.tabs` for distinct sections representing stages of the risk assessment lifecycle.
*   A prominent title "Operational Risk Assessment Lifecycle Simulator" will be displayed.
*   Each major section will correspond to a stage in the lifecycle, presenting related inputs, outputs, and visualizations.
*   The overall flow should mimic the "Risk Assessment Lifecycle" diagram from the PRMIA Handbook (page 21).

**Input Widgets and Controls:**
*   **Data Simulation Configuration (e.g., "Data Generation" section):**
    *   **Number of Events**: `st.slider` or `st.number_input` (e.g., 50 to 1000 events).
    *   **Date Range**: Two `st.date_input` widgets for `start_date` and `end_date`.
    *   **Business Units**: `st.multiselect` or `st.text_input` (comma-separated for user-defined units). Default values provided if left empty.
    *   **Risk Categories**: `st.multiselect` or `st.text_input` (comma-separated for user-defined categories). Default values provided if left empty.
    *   **Generate Data Button**: `st.button` to trigger `generate_synthetic_loss_data`.
*   **Risk Identification & Assessment (e.g., "Risk Input" section):**
    *   **Business Unit Name**: `st.text_input` to define the unit.
    *   **Inherent Risk Level**: `st.selectbox` with options `['High', 'Medium', 'Low']`.
    *   **Controls**: `st.text_area` or `st.multiselect` for users to list/select associated controls.
    *   **Control Effectiveness**: `st.selectbox` with options `['Effective', 'Partially Effective', 'Ineffective']`.
    *   **Control Attributes**: `st.multiselect` or `st.checkbox` for `['Preventative', 'Detective', 'Key', 'Non-Key', 'Manual', 'Automated']`.
    *   **Store Inputs Button**: `st.button` to trigger `store_risk_assessment_inputs`.
*   **Residual Risk Calculation (e.g., "Residual Risk" section):**
    *   **Inherent Risk Select**: `st.selectbox` populated with options `['High', 'Medium', 'Low']`.
    *   **Control Effectiveness Select**: `st.selectbox` populated with options `['Effective', 'Partially Effective', 'Ineffective']`.
    *   **Calculation Approach**: `st.selectbox` with options `['Simple', 'Weighted']`.
    *   The residual risk will be displayed dynamically as `st.write` or `st.markdown`.

**Visualization Components:**
*   **Loss Data Visualizations (e.g., "Loss Data Analysis" section):**
    *   **Trend Plot**: A line or area chart (e.g., Plotly `px.line` or `px.area`) showing `Loss_Amount` over `Timestamp`, with options to aggregate (e.g., daily, monthly).
    *   **Relationship Plot**: A scatter plot (e.g., Plotly `px.scatter`) to examine correlations, e.g., `Loss_Amount` vs. `Recovery_Time_Days`.
    *   **Aggregated Comparison**: Bar charts or heatmaps (e.g., Plotly `px.bar` or `px.imshow`) for categorical insights, e.g., total `Loss_Amount` by `Business_Unit` or `Risk_Category`.
    *   All plots will have clear titles, labeled axes, and legends. Adopt a color-blind-friendly palette and font size $\geq 12$ pt.
*   **Residual Risk Heatmap (e.g., "Residual Risk" section):**
    *   An interactive heatmap visualizing the residual risk matrix, dynamically updating based on the selected `approach` (`Simple` or `Weighted`). The matrix axes will be Inherent Risk and Control Effectiveness, with cell values representing Residual Risk.

**Interactive Elements and Feedback Mechanisms:**
*   All inputs should be interactive, with outputs (calculations, visualizations) updating in real-time as parameters change.
*   Streamlit's inherent reactivity will be utilized.
*   Feedback messages for user actions (e.g., "Data generated successfully!", "Risk assessment stored.").
*   Validation messages for inputs (e.g., if a required field is empty).

## 3. Additional Requirements

**Real-time Updates and Responsiveness:**
*   The application will leverage Streamlit's reactivity model to ensure that all calculations and visualizations update instantly when user inputs are modified.
*   Computationally intensive tasks (if any) will be optimized to meet the 5-minute execution constraint.

**Annotation and Tooltip Specifications:**
*   Each input widget and control will include inline help text or tooltips (`st.help`, `st.expander`, `st.info`) to describe its purpose and expected input format.
*   Explanations will be provided for calculated results, especially for residual risk, detailing how the inputs map to the outputs.
*   A "References" section will be included at the end of the application, crediting the PRMIA Operational Risk Manager Handbook and any other external datasets or libraries used.

## 4. Notebook Content and Code Requirements

This section details how the functions and concepts from the Jupyter Notebook will be integrated into the Streamlit application.

**1. Library Imports:**
The following libraries will be imported at the beginning of the Streamlit application script.
```python
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px # For interactive visualizations
```

**2. Global Variables / Session State:**
To maintain state across Streamlit reruns, `st.session_state` will be used for variables that need to persist, such as `risk_assessment_data` and the generated `loss_data`.
```python
# Initialize session state variables
if 'risk_assessment_data' not in st.session_state:
    st.session_state.risk_assessment_data = {}
if 'loss_data' not in st.session_state:
    st.session_state.loss_data = pd.DataFrame() # Initialize as empty DataFrame
```

**3. `generate_synthetic_loss_data` Function:**
*   **Purpose**: To create a synthetic dataset of operational loss events for analysis and visualization.
*   **Integration**: This function will be called within a dedicated section (e.g., "Loss Data Simulation"). User inputs will drive the parameters.
*   **Streamlit UI Components**:
    *   `num_events`: `st.number_input("Number of Loss Events to Simulate", min_value=100, max_value=10000, value=100)`
    *   `start_date`, `end_date`: `st.date_input("Simulation Date Range", value=[pd.to_datetime('2023-01-01'), pd.to_datetime('2023-12-31')])`
    *   `business_units`: `st.multiselect("Select Business Units (optional)", options=['BU1', 'BU2', 'BU3', 'BU4'], default=['BU1', 'BU2', 'BU3'])`
    *   `risk_categories`: `st.multiselect("Select Risk Categories (optional)", options=['RC1', 'RC2', 'RC3', 'RC4'], default=['RC1', 'RC2'])`
    *   `st.button("Generate Loss Data")` will trigger the function call and store the result in `st.session_state.loss_data`.
*   **Visualization**: After generation, `st.dataframe(st.session_state.loss_data.head())` will show a preview. Subsequent visualization sections will use `st.session_state.loss_data` for plotting (trend, scatter, bar charts).
*   **Code**:
    ```python
    def generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories):
        """Generates a synthetic dataset of operational loss events.
        
        Args:
            num_events (int): The number of loss events to generate.
            start_date (datetime.date): The start date for the events.
            end_date (datetime.datetime): The end date for the events.
            business_units (list): List of business unit names.
            risk_categories (list): List of risk category names.

        Returns:
            pandas.DataFrame: A DataFrame containing the synthetic loss data.
        """
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
    ```

**4. `calculate_residual_risk` Function:**
*   **Purpose**: To calculate the residual risk level based on inherent risk and control effectiveness, directly implementing the logic from the PRMIA handbook's look-up tables.
*   **Integration**: This function will be central to the "Residual Risk Calculation" section.
*   **Mathematical Formula**:
    $$R_{risk} = f(I_{risk}, C_{eff})$$
    where $R_{risk}$ is the Residual Risk, $I_{risk}$ is the Inherent Risk, and $C_{eff}$ is the Control Effectiveness.
*   **Streamlit UI Components**:
    *   `inherent_risk_input`: `st.selectbox("Select Inherent Risk Level", options=['High', 'Medium', 'Low'])`
    *   `control_effectiveness_input`: `st.selectbox("Select Control Effectiveness Level", options=['Effective', 'Partially Effective', 'Ineffective'])`
    *   `approach_input`: `st.selectbox("Select Calculation Approach", options=['Simple', 'Weighted'])`
    *   The calculated `residual_risk` will be displayed using `st.metric` or `st.write`.
*   **Heatmap Visualization**: An interactive heatmap (using Plotly) will represent the full risk matrix for the selected approach, allowing users to visually understand the mappings.
    *   For the heatmap, a DataFrame representing the `risk_matrix` would be constructed and then visualized using `px.imshow` or similar.
*   **Code**:
    ```python
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
    ```

**5. `store_risk_assessment_inputs` Function:**
*   **Purpose**: To store risk assessment details, supporting issue management and tracking.
*   **Integration**: This function will be used in the "Risk Identification" or "Control Assessment" sections to persist user-defined risks and controls.
*   **Streamlit UI Components**:
    *   Inputs for `unit_name`, `inherent_risk`, and `controls` as described in "Risk Identification & Assessment" in Section 2.
    *   A `st.button("Store Risk Assessment")` will call this function.
    *   `st.session_state.risk_assessment_data` will be updated and displayed (e.g., `st.dataframe` or `st.json`) to show current stored data.
*   **Code (modified for Streamlit session state)**:
    ```python
    def store_risk_assessment_inputs(unit_name, inherent_risk, controls, control_effectiveness=None, control_attributes=None):
        """Stores risk assessment details in Streamlit session state.
        
        Args:
            unit_name (str): Name of the business unit.
            inherent_risk (str): Inherent risk level ('High', 'Medium', 'Low').
            controls (list): List of associated controls.
            control_effectiveness (str, optional): Effectiveness level ('Effective', 'Partially Effective', 'Ineffective').
            control_attributes (list, optional): List of control attributes.
        """
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
    ```
    *Note: The `store_risk_assessment_inputs` function from the notebook was very basic. It has been slightly enhanced above to accommodate control effectiveness and attributes, which are discussed in the notebook's narrative and user requirements for the Streamlit app.*

**6. Data Validation (`validate_dataframe`)**:
*   **Observation**: The Jupyter Notebook mentions a `validate_dataframe` function in its narrative, but the actual Python code for this function is *not provided*.
*   **Implementation Note**: If data validation is deemed critical beyond the scope of synthetic data generation, a custom `validate_dataframe` function would need to be implemented separately. This function would typically check for expected column names, data types, primary-key uniqueness, and missing values in critical fields, as specified in the "Data Requirements" section. For the current scope, the synthetic data generation function produces a DataFrame that inherently conforms to an expected schema.

**7. Overall Streamlit Application Flow:**
The Streamlit application will logically present the sections:
*   **Welcome/Overview**: Introduction and learning outcomes.
*   **Simulate Loss Data**: Inputs for `generate_synthetic_loss_data`, display of generated data head, and plots (trend, scatter, aggregated).
*   **Define Risk Assessment Units / Top-down Workshops**: Inputs for `store_risk_assessment_inputs` focusing on `unit_name` and `inherent_risk`.
*   **Control Assessment**: Allow users to select a business unit and then define/assess controls, including `control_effectiveness` and `control_attributes`, updating `st.session_state.risk_assessment_data`.
*   **Calculate Residual Risk**: Interactive section to use `calculate_residual_risk` based on selected inherent risk and control effectiveness, displaying the result and the relevant risk matrix heatmap.
*   **Issue Management & Tracking**: A simple display or input area to show/add identified issues or action plans from the `risk_assessment_data`.
*   **References**: A dedicated section listing the PRMIA handbook and any other used resources.

By following this specification, the Streamlit application will effectively simulate the operational risk assessment lifecycle, providing an interactive and educational experience.
