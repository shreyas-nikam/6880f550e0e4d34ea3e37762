id: 6880f550e0e4d34ea3e37762_documentation
summary: Module3 Lab2 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Operational Risk Assessment Lifecycle Simulator

## Introduction and Application Overview
Duration: 00:05:00

Welcome to the QuLab Operational Risk Assessment Lifecycle Simulator Codelab!

In the dynamic world of finance, effectively managing operational risk is paramount. Operational risk, defined as the risk of loss resulting from inadequate or failed internal processes, people and systems, or from external events, can significantly impact a financial institution's stability and reputation. This Streamlit application provides an interactive simulation of the operational risk assessment lifecycle, drawing inspiration from the "PRMIA Operational Risk Manager Handbook".

**Key Learning Outcomes:**

*   Understand the key stages and iterative flow of a robust operational risk assessment program.
*   Learn how top-down risk identification (e.g., inherent risk assessment) informs bottom-up control assessment.
*   Explore the critical interplay between **Inherent Risk**, **Control Effectiveness**, and **Residual Risk**.
*   Recognize the importance of clear taxonomies, consistent tracking, and data-driven insights in effective risk management.

This codelab will guide you through the application's structure, core functionalities, and underlying code, equipping you with the knowledge to understand, extend, and even build your own interactive risk management tools.

<aside class="positive">
Understanding operational risk is not just for risk managers; it's crucial for anyone involved in business operations, compliance, or finance to ensure organizational resilience.
</aside>

### Application Architecture Overview

The application follows a modular structure, typical for Streamlit applications that grow beyond a single file:

*   **`app.py`**: This is the main entry point of the application. It handles the overall layout, sidebar navigation, and routes user requests to specific functional pages.
*   **`application_pages/` directory**: This directory contains individual Python scripts, each responsible for rendering a specific section or "page" of the application (e.g., `overview.py`, `loss_data_simulation.py`, `risk_assessment.py`). This modularity makes the application easier to manage, debug, and extend.

<pre>
app.py (Main Application)
├── application_pages/
│   ├── overview.py (Explains app purpose)
│   ├── loss_data_simulation.py (Simulates risk events)
│   └── risk_assessment.py (Performs risk calculations)
</pre>

The application leverages Streamlit's `st.session_state` to maintain data persistence across user interactions and page navigations within a single user session, ensuring a smooth and consistent experience.

## Setting up the Development Environment
Duration: 00:05:00

Before running the application, you need to set up your Python environment and install the necessary libraries.

1.  **Prerequisites**:
    *   Python 3.7+ installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
    *   `pip` (Python package installer), which usually comes with Python.

2.  **Create a Project Directory**:
    Create a new directory for your project and navigate into it.

    ```bash
    mkdir qulab_risk_simulator
    cd qulab_risk_simulator
    ```

3.  **Create the Application Files**:
    Create the `app.py` file and the `application_pages` directory with its Python files as provided in the problem description.

    *   `app.py`
    *   `application_pages/overview.py`
    *   `application_pages/loss_data_simulation.py`
    *   `application_pages/risk_assessment.py`

    Copy the respective code into these files.

4.  **Create a Virtual Environment (Recommended)**:
    Virtual environments help manage dependencies for different projects, avoiding conflicts.

    ```bash
    python -m venv venv
    ```

5.  **Activate the Virtual Environment**:
    *   **On Windows**:
        ```powershell
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

6.  **Install Dependencies**:
    The application requires `streamlit`, `pandas`, `numpy`, and `plotly`.

    ```bash
    pip install streamlit pandas numpy plotly
    ```

7.  **Run the Application**:
    Once all dependencies are installed, you can run the Streamlit application from your terminal.

    ```bash
    streamlit run app.py
    ```

    Your default web browser should open, displaying the Streamlit application.

<aside class="positive">
Always use a virtual environment for your Python projects. It isolates your project dependencies, preventing conflicts and ensuring reproducibility.
</aside>

## Exploring the Overview Page
Duration: 00:03:00

The "Overview" page serves as the initial landing page and provides essential context about the application's purpose and objectives. This is crucial for new users to understand what the simulator aims to achieve.

When you run `app.py`, the `st.sidebar.selectbox` defaults to "Overview", which triggers the import and execution of the `run_overview()` function from `application_pages/overview.py`.

Let's look at the relevant code snippet from `app.py`:

```python
# app.py snippet
page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Loss Data Simulation", "Risk Assessment"])
if page == "Overview":
    from application_pages.overview import run_overview
    run_overview()
# ... other elifs
```

And the content of `application_pages/overview.py`:

```python
# application_pages/overview.py
import streamlit as st

def run_overview():
    st.header("Overview")
    st.markdown("""
    This application simulates the operational risk assessment lifecycle, providing an interactive and educational experience.

    **Purpose and Objectives:**
    The primary purpose of this Streamlit application is to provide an interactive simulation of the operational risk assessment lifecycle within a financial institution, as described in the "PRMIA Operational Risk Manager Handbook". The application aims to educate risk management students, junior risk professionals, and business unit managers by offering a practical, hands-on understanding of how risks are identified, assessed, controlled, and monitored in an iterative process.

    **Key Learning Outcomes:**
    *   Understand the key stages and flow of a robust operational risk assessment program.
    *   Learn how top-down risk identification informs bottom-up control assessment.
    *   Explore the interplay between inherent risk, control effectiveness, and residual risk.
    *   Recognize the importance of clear taxonomies and consistent tracking in risk management.
    """)
```

The `run_overview()` function simply uses `st.header()` for the main title and `st.markdown()` to display formatted text, including bolding for emphasis. This static content provides the foundational understanding before diving into the interactive simulations.

<aside class="positive">
A clear and concise overview is vital for any application. It sets user expectations and explains the value proposition, especially for educational tools.
</aside>

## Simulating Loss Data
Duration: 00:10:00

The "Loss Data Simulation" page allows users to generate synthetic operational loss events. This data is crucial for understanding the frequency and severity of losses, which in turn informs risk assessments.

Navigate to "Loss Data Simulation" using the sidebar.

The core logic for this page resides in `application_pages/loss_data_simulation.py`.

```python
# application_pages/loss_data_simulation.py snippets

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

        loss_amount = np.random.normal(10000, 5000) # Simulates loss amounts with a normal distribution
        near_miss_flag = np.random.choice([True, False], p=[0.1, 0.9]) # 10% chance of a near miss
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

    # User inputs for simulation parameters
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
```

### How it Works:

1.  **User Inputs**:
    *   `st.number_input()`: For the desired number of loss events.
    *   `st.date_input()`: To select the date range for the simulation.
    *   `st.multiselect()`: To optionally filter and select specific Business Units and Risk Categories. If no options are selected, default categories are used.

2.  **`generate_synthetic_loss_data` Function**:
    *   This function generates a `pandas.DataFrame` with synthetic loss event data.
    *   It simulates various attributes like `Timestamp`, `Business_Unit`, `Risk_Category`, `Loss_Amount` (using a normal distribution), `Near_Miss_Flag`, `Control_Breach_Type`, and `Recovery_Time_Days`.
    *   The use of `np.random.choice` and `np.random.normal` ensures that the data has a degree of randomness, mimicking real-world variability.

3.  **`st.session_state` for Data Persistence**:
    *   The `loss_data` DataFrame is stored in `st.session_state.loss_data`. This is crucial because Streamlit reruns the script from top to bottom on every interaction. Without `st.session_state`, the generated data would be lost after each button click or input change.
    *   The `if 'loss_data' not in st.session_state:` check ensures `loss_data` is initialized as an empty DataFrame when the application first starts or refreshes.

4.  **Data Generation and Display**:
    *   When the "Generate Loss Data" button is clicked, the `generate_synthetic_loss_data` function is called, and its output is stored in `st.session_state.loss_data`.
    *   `st.dataframe(st.session_state.loss_data.head())` shows a preview of the generated data.

5.  **Visualizations with Plotly Express**:
    *   The page generates three interactive plots using `plotly.express`:
        *   **Loss Amount Trend (Line Chart)**: `px.line()` visualizes `Loss_Amount` over `Timestamp`, helping identify any temporal patterns or anomalies.
        *   **Loss Amount vs. Recovery Time (Scatter Plot)**: `px.scatter()` shows the relationship between `Loss_Amount` and `Recovery_Time_Days`, which could highlight if longer recovery times correlate with higher losses.
        *   **Total Loss Amount by Business Unit (Bar Chart)**: `px.bar()` aggregates losses by `Business_Unit` to compare their total operational risk exposure.
    *   `st.plotly_chart(fig, use_container_width=True)` renders the interactive Plotly figures within the Streamlit application.

<aside class="negative">
The `generate_synthetic_loss_data` function uses simple random distributions. For real-world risk analysis, more sophisticated statistical models (e.g., compound Poisson processes for frequency and heavy-tailed distributions for severity) would be necessary to accurately simulate operational losses.
</aside>

## Performing Risk Assessment
Duration: 00:15:00

The "Risk Assessment" page is where the core concepts of inherent risk, control effectiveness, and residual risk are put into practice. It allows users to define risk assessment units, store their characteristics, and calculate residual risk based on a defined matrix.

Navigate to "Risk Assessment" using the sidebar.

The main logic is in `application_pages/risk_assessment.py`.

```python
# application_pages/risk_assessment.py snippets

import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_residual_risk(inherent_risk_level, control_effectiveness_level, approach):
    """Calculates residual risk based on inherent risk, control effectiveness, and approach."""
    # This matrix defines how inherent risk and control effectiveness combine to form residual risk.
    # It's a simplified representation of a risk heat map or matrix.
    if approach == "Simple" or approach == "Weighted": # Currently, both approaches use the same matrix
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

def store_risk_assessment_inputs(unit_name, inherent_risk, controls): # Simplified for current UI
    """Stores risk assessment details in Streamlit session state."""
    if not isinstance(controls, list):
        controls_list = [c.strip() for c in controls.split(',')] if controls else []
    else:
        controls_list = controls

    # Initialize if unit_name is new
    if unit_name not in st.session_state.risk_assessment_data:
        st.session_state.risk_assessment_data[unit_name] = {
            "inherent_risk": inherent_risk,
            "controls": {}
        }

    # Add/update controls with placeholder effectiveness/attributes (not collected from UI yet)
    for control_name in controls_list:
        st.session_state.risk_assessment_data[unit_name]["controls"][control_name] = {
            "effectiveness": None, # Not collected via UI on this page
            "attributes": []     # Not collected via UI on this page
        }

    # Always update inherent risk for the unit
    st.session_state.risk_assessment_data[unit_name]["inherent_risk"] = inherent_risk

    st.success(f"Risk assessment for '{unit_name}' stored successfully!")
    st.json(st.session_state.risk_assessment_data) # Display current state for debugging/understanding


def run_risk_assessment():
    st.header("Risk Assessment")

    # Initialize session state variable for storing risk assessments
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
    # Define the risk matrix for visualization.
    # Rows: Inherent Risk (High, Medium, Low)
    # Columns: Control Effectiveness (Ineffective, Partially Effective, Effective)
    data = [
        ["High", "Medium", "Low"], # Inherent: High
        ["Medium", "Medium", "Low"], # Inherent: Medium
        ["Low", "Low", "Low"],   # Inherent: Low
    ]
    # Note: The provided code has some redundancy, and the "Weighted" matrix is identical to "Simple".
    # This might be a placeholder for future, more complex weighted calculations.
    # The actual values for the heatmap are derived from the risk_matrix in calculate_residual_risk.
    # Let's align the heatmap with the function's output logic.
    # Risk matrix: (Inherent, ControlEff) -> Residual
    # High + Ineffective = High
    # High + Partially Effective = Medium
    # High + Effective = Low
    # Medium + Ineffective = Medium
    # Medium + Partially Effective = Medium
    # Medium + Effective = Low
    # Low + Ineffective = Low
    # Low + Partially Effective = Low
    # Low + Effective = Low

    # Rebuilding `data` to accurately reflect the `risk_matrix`
    data = [
        # Ineffective, Partially Effective, Effective
        [calculate_residual_risk("High", "Ineffective", approach_input), calculate_residual_risk("High", "Partially Effective", approach_input), calculate_residual_risk("High", "Effective", approach_input)], # Inherent: High
        [calculate_residual_risk("Medium", "Ineffective", approach_input), calculate_residual_risk("Medium", "Partially Effective", approach_input), calculate_residual_risk("Medium", "Effective", approach_input)], # Inherent: Medium
        [calculate_residual_risk("Low", "Ineffective", approach_input), calculate_residual_risk("Low", "Partially Effective", approach_input), calculate_residual_risk("Low", "Effective", approach_input)], # Inherent: Low
    ]

    df = pd.DataFrame(data, columns=["Ineffective", "Partially Effective", "Effective"], index = ["High", "Medium", "Low"])

    # Map risk levels to a numerical scale for color intensity in heatmap for better visualization
    # This is often done for 'RdYlGn' (Red-Yellow-Green) where higher numbers are greener/safer.
    # But for risk, often Red=High, Green=Low. So we can reverse the mapping if needed for `RdYlGn`.
    # Let's use a common mapping: High=3, Medium=2, Low=1
    risk_level_map = {"High": 3, "Medium": 2, "Low": 1}
    df_numeric = df.applymap(lambda x: risk_level_map.get(x, x)) # Apply mapping to data frame values

    fig = px.imshow(df_numeric,
                    labels=dict(x="Control Effectiveness", y="Inherent Risk", color="Residual Risk Numeric Value"),
                    x=df.columns,
                    y=df.index,
                    color_continuous_scale=[(0, "red"), (0.5, "yellow"), (1, "green")], # Explicitly define a custom scale for High=Red, Medium=Yellow, Low=Green
                    text_auto=True, # Display the text values on the heatmap cells
                   )
    # Customize color scale range to match risk levels if needed for specific scales
    fig.update_coloraxes(showscale=False) # Hide the default color scale bar
    st.plotly_chart(fig, use_container_width=True)
```

### How it Works:

1.  **`st.session_state` for Risk Assessment Data**:
    *   `st.session_state.risk_assessment_data` is initialized as an empty dictionary. This will store all the defined risk assessment units, allowing users to build a collection of assessments during their session.

2.  **Define Risk Assessment Units**:
    *   `st.text_input("Business Unit Name")`: Allows users to name the risk unit being assessed.
    *   `st.selectbox("Inherent Risk Level", ...)`: Users select the inherent risk (risk before controls) as High, Medium, or Low.
    *   `st.text_area("Controls (comma-separated)")`: Users list relevant controls for the unit.
    *   **`store_risk_assessment_inputs` Function**:
        *   This function is called when "Store Risk Assessment" is clicked.
        *   It stores the `unit_name`, `inherent_risk`, and `controls` into `st.session_state.risk_assessment_data`.
        *   The `controls` are parsed from a comma-separated string into a list and stored as a dictionary, allowing for future expansion to include details like individual control effectiveness or attributes.
        *   `st.json()` is used to display the current state of `st.session_state.risk_assessment_data`, which is helpful for developers to see the stored structure.

3.  **Calculate Residual Risk**:
    *   Users select an `Inherent Risk Level`, `Control Effectiveness Level` (Effective, Partially Effective, Ineffective), and a `Calculation Approach` ("Simple" or "Weighted").
    *   **`calculate_residual_risk` Function**:
        *   This function implements a **risk matrix**. It takes `inherent_risk_level` and `control_effectiveness_level` as inputs and returns the `Residual Risk` based on a predefined mapping.
        *   **Inherent Risk** is the level of risk existing if no controls were in place.
        *   **Control Effectiveness** is how well the implemented controls mitigate the inherent risk.
        *   **Residual Risk** is the risk remaining *after* controls have been applied.
        *   The current implementation of "Simple" and "Weighted" approaches uses the exact same `risk_matrix`. In a more advanced application, the "Weighted" approach might incorporate different weights or formulas for control effectiveness.
        *   The result is displayed using `st.markdown()`.

4.  **Residual Risk Heatmap Visualization**:
    *   `st.subheader("Residual Risk Heatmap")`
    *   A `pandas.DataFrame` is constructed to represent the risk matrix visually.
    *   The `px.imshow()` function from Plotly Express is used to create an interactive heatmap.
    *   The `color_continuous_scale` is customized to map "High" risk to Red, "Medium" to Yellow, and "Low" to Green, providing an intuitive visual representation of risk levels. To achieve this, the text labels ("High", "Medium", "Low") are mapped to numerical values (e.g., 3, 2, 1) to allow Plotly's continuous color scale to apply.
    *   `text_auto=True` ensures that the actual risk levels (e.g., "High", "Medium", "Low") are displayed directly on the heatmap cells, making it very readable.

<aside class="positive">
The concept of a **Risk Matrix** (also known as a Heatmap) is fundamental in risk management. It provides a visual, intuitive way to assess and prioritize risks based on their likelihood and impact, or in this case, inherent risk and control effectiveness.
</aside>

## Understanding the Application Architecture and Flow
Duration: 00:07:00

Now that we've explored each page, let's consolidate our understanding of the application's overall architecture and how data flows within it.

### Core Architectural Principles:

1.  **Modularity**: The application is broken down into `app.py` (the main orchestrator) and specific `application_pages` modules. This design promotes:
    *   **Organization**: Code for different functionalities is separated.
    *   **Maintainability**: Changes to one page are less likely to impact others.
    *   **Scalability**: New features can be added as new pages without cluttering the main script.

2.  **Session State Management**: Streamlit's stateless nature (rerunning the script on every interaction) is elegantly handled by `st.session_state`.
    *   `st.session_state.loss_data`: Stores the DataFrame generated by the "Loss Data Simulation" page. This allows the data to persist even if the user navigates away and comes back.
    *   `st.session_state.risk_assessment_data`: Stores the dictionary of defined risk assessment units. This enables building up a list of assessments throughout a session.

### Application Flow:

```
+-+
|    app.py      |
| (Main Dispatcher) |
+-+
        |
        | 1. Select Navigation (Sidebar)
        V
+-+
|   st.sidebar.selectbox("Navigation", ...)     |
+-+
        |
        | 2. Route to selected page
        V
+-+
|   Option A: "Overview"      |   Option B: "Loss Data Simulation"   |   Option C: "Risk Assessment"  |
| (application_pages/overview.py) | (application_pages/loss_data_simulation.py) | (application_pages/risk_assessment.py) |
|                                 |                                    |                                |
|   - Displays static text        |   - User inputs parameters       |   - User defines risk units    |
|   - Explains purpose/objectives |   - Calls generate_synthetic_loss_data() |   - Calls store_risk_assessment_inputs() |
|                                 |   - Stores data in st.session_state.loss_data |   - Stores data in st.session_state.risk_assessment_data |
|                                 |   - Displays data preview        |   - User selects inherent risk/control effectiveness |
|                                 |   - Visualizes data (Plotly)     |   - Calls calculate_residual_risk() |
|                                 |                                    |   - Displays residual risk     |
|                                 |                                    |   - Visualizes risk matrix (Plotly) |
+-+
```

### Importance of the Design:

*   **User Experience**: The clear navigation and persistent data via `st.session_state` make the application feel cohesive and responsive, despite Streamlit's underlying execution model.
*   **Developer Experience**: Modular files make it easier for developers to work on specific features without interfering with other parts of the application. The use of functions within each page script (`run_overview`, `run_loss_data_simulation`, `run_risk_assessment`) further enhances code organization.
*   **Data Flow**: Data (like `loss_data` or `risk_assessment_data`) generated or modified on one page is accessible and maintained when navigating to other pages within the same session, enabling more complex multi-step workflows.

<aside class="positive">
Always think about how data will persist and flow between different parts of your Streamlit application. `st.session_state` is your primary tool for this within a single user session.
</aside>

## Further Enhancements and Next Steps
Duration: 00:05:00

This QuLab simulator provides a solid foundation for understanding operational risk assessment. Here are some ideas for further enhancements and next steps to make it even more powerful and realistic:

1.  **Persistent Data Storage**:
    *   Currently, all data (simulated losses, stored assessments) is lost when the Streamlit application restarts or the user session ends.
    *   **Enhancement**: Integrate a database (e.g., SQLite for local development, PostgreSQL/MySQL for deployment) to store `loss_data` and `risk_assessment_data` persistently. This would allow users to save their simulations and analyses.

2.  **More Sophisticated Risk Models**:
    *   The `generate_synthetic_loss_data` function uses simple normal distributions.
    *   **Enhancement**: Implement more realistic distributions for loss frequency (e.g., Poisson, Negative Binomial) and loss severity (e.g., Log-normal, Pareto, GPD), often found in **Loss Distribution Approach (LDA)** models for OpRisk.
    *   **Enhancement**: Introduce correlation between different risk factors or business units.
    *   The `calculate_residual_risk` function's "Weighted" approach is currently identical to "Simple".
    *   **Enhancement**: Implement a truly weighted approach, perhaps allowing users to define weights for control attributes or to incorporate a numerical scoring system for inherent risk and control effectiveness.

3.  **Advanced Control Assessment**:
    *   The "Define Risk Assessment Units" currently accepts controls as a comma-separated string.
    *   **Enhancement**: Create a dedicated interface to define individual controls with attributes like `Control Type` (Preventive/Detective), `Control Owner`, `Frequency of Review`, `Testing Results`, and **Control Effectiveness Rating** (e.g., a specific numerical score or a more granular qualitative rating). This could feed directly into the `calculate_residual_risk` function.

4.  **Scenario Analysis**:
    *   **Enhancement**: Allow users to define specific "scenarios" (e.g., a major cyber-attack, a regulatory breach) and model their potential impact on operational losses, leveraging the simulation engine.

5.  **User Authentication and Multi-User Support**:
    *   **Enhancement**: For a production-ready application, implement user authentication to allow multiple users to manage their own risk portfolios securely.

6.  **Drill-down Capabilities**:
    *   **Enhancement**: In the visualizations, allow users to click on bars or points to "drill down" and see the underlying data or related assessments.

7.  **Integration with External Data**:
    *   **Enhancement**: Simulate or integrate with external operational risk event databases or industry loss data consortia.

8.  **Risk Treatment Planning**:
    *   **Enhancement**: Add a section where users can propose and track **risk treatment plans** (e.g., avoid, reduce, transfer, accept) for high residual risks.

Feel free to download the code and experiment with these enhancements. The modular structure of the application makes it an ideal playground for learning and building!

<button>
  [Download App Code (simulated)](https://example.com/qulab_risk_simulator.zip)
</button>

<aside class="positive">
The journey of building applications is iterative. Start with a functional core, then continuously add features and refine the user experience based on feedback and new requirements.
</aside>
