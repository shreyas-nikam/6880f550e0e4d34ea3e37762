
# Technical Specification: Operational Risk Assessment Lifecycle Simulator Jupyter Notebook

## 1. Notebook Overview

This Jupyter Notebook provides an interactive simulation of the operational risk assessment lifecycle within a financial institution, drawing insights from the "PRMIA Operational Risk Manager Handbook" [1]. It aims to offer a practical, hands-on understanding of how operational risks are identified, assessed, controlled, and monitored in an iterative process.

### Learning Goals

*   Understand the key stages and the iterative flow of a robust operational risk assessment program.
*   Learn how top-down risk identification informs and prioritizes bottom-up control assessment.
*   Explore the interplay between inherent risk, control effectiveness, and the resulting residual risk through interactive scenarios.
*   Recognize the importance of clear risk and control taxonomies, as well as consistent tracking, in effective operational risk management.
*   Gain insights into data-driven approaches for understanding and visualizing operational risk trends and relationships.

### Expected Outcomes

Upon completion of this notebook, users will be able to:
*   Articulate the sequential steps of an operational risk assessment lifecycle.
*   Qualitatively assess inherent risks and control effectiveness for various operational risk scenarios.
*   Apply a defined methodology to calculate residual risk based on inherent risk and control effectiveness.
*   Interpret and analyze visualizations of residual risk, loss events, and near misses.
*   Identify potential control gaps and propose basic action plans for risk mitigation.
*   Understand the key insights contained in the uploaded document and supporting data.

### Scope & Constraints

*   The notebook must be executable end-to-end on a mid-spec laptop (8 GB RAM) in fewer than 5 minutes.
*   Only open-source Python libraries available on PyPI may be used.
*   All major steps will include both descriptive markdown cells and well-commented code cells, clearly explaining **what** is happening and **why**.
*   The notebook will focus solely on the simulation and analysis, excluding deployment steps or platform-specific references.

## 2. Mathematical and Theoretical Foundations

This section outlines the core concepts and mathematical logic underpinning the operational risk assessment simulation.

### 2.1 Operational Risk Assessment Lifecycle

The operational risk assessment lifecycle is an iterative process, as described in [1, "The Risk Assessment Lifecycle" diagram, page 21]. Key stages include:
*   **Define Risk Assessment Units:** Establishing the organizational or process boundaries for risk assessment.
*   **Top-down Workshops (Risk Identification):** Identifying and prioritizing inherent risks at a high level.
*   **Identify Controls:** Linking identified risks to existing or proposed controls.
*   **Process Reviews:** Mapping and analyzing processes to understand vulnerabilities and control points.
*   **Control Substantiation:** Assessing the design and implementation effectiveness of controls.
*   **Identify Issues:** Pinpointing control deficiencies or gaps.
*   **Design Action Plans:** Developing plans to address identified issues.
*   **Oversight & Monitoring:** Continuous tracking of the risk environment, losses, and action plan progress.
*   **Management Validation:** Senior management review and approval of the risk profile.

### 2.2 Inherent Risk

Inherent risk ($I_{risk}$) is defined as the level of risk before any controls or mitigations have been applied. It represents the raw risk exposure.
In this simulation, inherent risk will be assessed qualitatively based on categories such as likelihood and impact. Users will assign qualitative levels:
*   **High:** Significant potential impact and/or high probability of occurrence.
*   **Medium:** Moderate potential impact and/or moderate probability of occurrence.
*   **Low:** Minor potential impact and/or low probability of occurrence.

### 2.3 Control Effectiveness

Control effectiveness ($C_{eff}$) is the degree to which a control successfully mitigates or detects a risk. Users will assess controls based on simulated scenarios, considering attributes like:
*   **Preventative vs. Detective:** Preventative controls aim to stop an event from occurring, while detective controls aim to identify an event after it has occurred.
*   **Key vs. Non-Key:** Key controls are primary mitigators, while non-key controls are supplementary.
*   **Manual vs. Automated:** Manual controls rely on human intervention, automated controls are system-driven.

The effectiveness will be rated qualitatively:
*   **Effective:** The control is well-designed and consistently implemented to mitigate the associated risk.
*   **Partially Effective:** The control has design or implementation weaknesses, or its effectiveness is inconsistent.
*   **Ineffective:** The control is poorly designed, not implemented, or consistently fails to mitigate the associated risk.

### 2.4 Residual Risk Calculation

Residual risk ($R_{risk}$) is the remaining risk after controls have been applied and are considered effective. The calculation is not a simple subtraction but a mapping function based on lookup tables, as illustrated in [1, "Two Sample Approaches for Residual Risk Rating", page 38].

The general form of the relationship is:
$$R_{risk} = f(I_{risk}, C_{eff})$$
where $I_{risk}$ is the Inherent Risk and $C_{eff}$ is the Control Effectiveness.

Two sample approaches for mapping inherent risk and control effectiveness to residual risk are provided:

**Approach 1: Residual Risk Chart (Simple)**

| Inherent Risk | Control Effectiveness: Effective | Control Effectiveness: Partially Effective | Control Effectiveness: Ineffective |
| :------------ | :------------------------------- | :--------------------------------------- | :------------------------------- |
| High          | Low                              | Medium                                   | High                             |
| Medium        | Low                              | Medium                                   | Medium                           |
| Low           | Low                              | Low                                      | Low                              |

**Approach 2: Residual Risk Chart with Control Weighting (Recommended when risk is high for violations of law)**

| Inherent Risk | Control Effectiveness: Effective | Control Effectiveness: Partially Effective | Control Effectiveness: Ineffective |
| :------------ | :------------------------------- | :--------------------------------------- | :------------------------------- |
| High          | Low                              | Medium                                   | High                             |
| Medium        | Low                              | Medium                                   | High                             |
| Low           | Low                              | Medium                                   | Medium                           |

The function $f$ in this context performs a lookup within these matrices. For instance, if $I_{risk} = \text{High}$ and $C_{eff} = \text{Effective}$, then using Approach 1, $R_{risk} = \text{Low}$.

### 2.5 Issue Management

Issues arise from ineffective controls or identified control gaps. An issue management process involves:
*   Identifying the issue and its root cause.
*   Designing an action plan with specific steps, ownership, and deadlines.
*   Monitoring progress and escalating delays.
*   Implementing compensating controls if necessary.

### 2.6 Dynamic Data Simulation

To support trend and aggregated comparison visualizations, synthetic data for "loss events" and "near misses" will be generated. This data will include:
*   **Loss Events:** Incidents resulting in financial or non-financial loss.
*   **Near Misses:** Incidents that could have resulted in loss but were mitigated or avoided.

The data will incorporate realistic numeric (e.g., loss amount, recovery time), categorical (e.g., business unit, risk category, control breach type), and time-series fields (e.g., timestamp of event).

## 3. Code Requirements

This section specifies the expected libraries, input/output, algorithms, and visualizations for the Jupyter Notebook.

### 3.1 Expected Libraries

The following open-source Python libraries (from PyPI) are expected for data handling, numerical operations, user interaction, and visualization:
*   **`pandas`**: For data manipulation, loading, and structuring of synthetic data.
*   **`numpy`**: For numerical operations, especially for synthetic data generation.
*   **`matplotlib.pyplot`**: For static plotting.
*   **`seaborn`**: For enhanced statistical data visualization.
*   **`ipywidgets`**: For creating interactive user interface elements (sliders, dropdowns, text inputs, buttons).
*   **`datetime` / `random`**: (Standard Python libraries) For generating realistic time-series and random data.

### 3.2 Input/Output Expectations

#### 3.2.1 Inputs

The notebook will primarily rely on user inputs and dynamically generated synthetic data.
*   **User Inputs (via `ipywidgets`):**
    *   **Risk Assessment Unit Definition:** Text inputs for unit names, dropdowns for type (e.g., "Business Line", "Process Based").
    *   **Inherent Risk Identification:** Dropdowns (e.g., "Internal Fraud", "System Failure"), qualitative sliders/dropdowns (High, Medium, Low) for perceived inherent risk.
    *   **Control Definition:** Text inputs for control descriptions, dropdowns for attributes (Preventative/Detective, Key/Non-Key, Manual/Automated), qualitative sliders/dropdowns (Effective, Partially Effective, Ineffective) for control effectiveness.
    *   **Residual Risk Calculation Method:** Radio buttons or dropdown to select "Approach 1 (Simple)" or "Approach 2 (Weighted)".
    *   **Issue Tracking:** Text areas for "Issue Description" and "Action Plan".
    *   **Synthetic Data Parameters:** Sliders or text inputs for controlling scale/range of generated data (e.g., number of events, average loss amount, date range).
    *   **Visualization Parameters:** Dropdowns/sliders for filtering data or adjusting plot aesthetics.
*   **Optional Sample Dataset:**
    *   A lightweight, pre-generated sample CSV file (≤ 5 MB) for loss events and near misses.
    *   Expected columns: `Timestamp` (datetime), `Business_Unit` (categorical), `Risk_Category` (categorical, e.g., "Internal Fraud", "System Failure"), `Loss_Amount` (numeric), `Near_Miss_Flag` (boolean), `Control_Breach_Type` (categorical, e.g., "Process", "People", "System", "External").
    *   The notebook should confirm expected column names, data types, and primary-key uniqueness (e.g., `Timestamp` + `Business_Unit` for unique event).
    *   It should assert no missing values in critical fields (`Loss_Amount`, `Risk_Category`).
    *   Log summary statistics for numeric columns.

#### 3.2.2 Outputs

*   **Interactive Tables:** Display of user-defined inherent risks, controls, and calculated residual risks.
*   **Visualizations:** Charts and plots as specified in section 3.4.
*   **Summary Statistics:** For generated or loaded synthetic data.
*   **Textual Feedback:** Messages confirming user inputs, calculation results, or data validation outputs.

### 3.3 Algorithms or Functions to be Implemented (without code)

#### 3.3.1 Data Generation Functions

*   **`generate_synthetic_loss_data(num_events, start_date, end_date, business_units, risk_categories)`:**
    *   Purpose: Creates a synthetic dataset of operational loss events and near misses.
    *   Inputs: Number of events, date range, lists of possible business units and risk categories.
    *   Output: Pandas DataFrame with `Timestamp`, `Business_Unit`, `Risk_Category`, `Loss_Amount`, `Near_Miss_Flag`, `Control_Breach_Type`, `Recovery_Time_Days` (numeric).
    *   Logic: Randomly generates values for each field, ensuring realistic distributions (e.g., log-normal for `Loss_Amount`).

#### 3.3.2 Risk Assessment Logic Functions

*   **`calculate_residual_risk(inherent_risk_level, control_effectiveness_level, approach)`:**
    *   Purpose: Determines residual risk based on inherent risk and control effectiveness using a lookup table approach.
    *   Inputs: String representing `inherent_risk_level` ('High', 'Medium', 'Low'), string representing `control_effectiveness_level` ('Effective', 'Partially Effective', 'Ineffective'), and string `approach` ('Simple', 'Weighted').
    *   Output: String representing the `residual_risk_level` ('High', 'Medium', 'Low').
    *   Logic: Implements the lookup logic from the tables provided in Section 2.4.

*   **`store_risk_assessment_inputs(unit_name, inherent_risk, controls)`:**
    *   Purpose: Stores user-defined risk assessment details in an in-memory data structure (e.g., a list of dictionaries or a DataFrame).
    *   Inputs: `unit_name` (string), `inherent_risk` (string), and a list of `control` dictionaries (each containing `description`, `type`, `effectiveness`).
    *   Output: Updates an internal data store.

#### 3.3.3 Data Validation Functions

*   **`validate_dataframe(df, expected_columns, expected_dtypes, critical_columns)`:**
    *   Purpose: Checks for expected column names, data types, and missing values in critical fields.
    *   Inputs: DataFrame `df`, dictionary `expected_columns` (column name: expected dtype), list `critical_columns`.
    *   Output: Boolean (True if valid, False otherwise), and logs detailed validation results/warnings.

### 3.4 Visualizations

Visualizations will adhere to color-blind-friendly palettes (e.g., from Seaborn's default palettes), use font size ≥ 12 pt, and include clear titles, labeled axes, and legends. Interactivity will be enabled where supported (e.g., Matplotlib's interactive backend, or via `ipywidgets` refreshing plots), with static PNG fallbacks.

#### 3.4.1 Core Visuals

1.  **Trend Plot (Line or Area Chart) for Loss Events over Time:**
    *   Purpose: Visualize the historical pattern of simulated loss events or total loss amounts.
    *   Data Source: Synthetic loss event data.
    *   X-axis: Time (e.g., `Timestamp` aggregated by month/quarter).
    *   Y-axis: Total `Loss_Amount` or Count of events.
    *   Segmentation: Option to segment by `Business_Unit` or `Risk_Category` using different colored lines/areas.
    *   Interactivity: Slider for date range selection, dropdown for aggregation level (daily, weekly, monthly).

2.  **Relationship Plot (Scatter Plot) for Loss Amount vs. Recovery Time:**
    *   Purpose: Examine potential correlations between the severity of a loss event and the time taken to recover.
    *   Data Source: Synthetic loss event data.
    *   X-axis: `Recovery_Time_Days`.
    *   Y-axis: `Loss_Amount` (potentially on a logarithmic scale if data is skewed).
    *   Segmentation: Color-code points by `Risk_Category` or `Control_Breach_Type`.
    *   Annotations: Optionally highlight key events (e.g., highest loss events).

3.  **Aggregated Comparison (Bar Chart or Heatmap) for Categorical Insights:**
    *   **Bar Chart: Total Loss by Risk Category / Business Unit:**
        *   Purpose: Compare total loss amounts across different operational risk categories or business units.
        *   Data Source: Synthetic loss event data.
        *   X-axis: Categorical variable (e.g., `Risk_Category` or `Business_Unit`).
        *   Y-axis: Sum of `Loss_Amount`.
        *   Sorting: Bars sorted in descending order of `Loss_Amount`.
    *   **Heatmap: Residual Risk Matrix:**
        *   Purpose: Visually represent the calculated residual risk levels for user-defined scenarios.
        *   Data Source: Programmatically generated matrix based on user's inherent risk and control effectiveness inputs.
        *   Axes: Inherent Risk (rows), Control Effectiveness (columns).
        *   Cells: Color-coded based on the resulting `Residual_Risk_Level` (e.g., Red for High, Amber for Medium, Green for Low).
        *   Labels: Display the residual risk level string (High, Medium, Low) within each cell.
        *   Interactivity: Plot dynamically updates based on user selection of the residual risk calculation `approach` (Simple or Weighted).

#### 3.4.2 Supplementary Visuals

*   **Tables of User Inputs:** Clearly display all user-defined inherent risks, controls, and their assessed effectiveness in a tabular format.
*   **Issue Tracking Table:** A simple table listing identified issues and their associated action plans, owners, and status.

## 4. Additional Notes or Instructions

### 4.1 Assumptions

*   Users have a basic understanding of Jupyter Notebooks and Python.
*   The qualitative risk levels (High, Medium, Low) for inherent and residual risk, and effectiveness levels (Effective, Partially Effective, Ineffective) are ordinal and can be mapped numerically for internal calculations if needed (e.g., 3, 2, 1).
*   The "PRMIA Operational Risk Manager Handbook" serves as the primary theoretical reference for concepts and the residual risk lookup logic.
*   The synthetic data generated will be plausible but not necessarily representative of any specific real-world financial institution's loss data.

### 4.2 Constraints

*   No external data sources beyond the optional sample CSV should be required for full notebook execution.
*   All interactive elements must use `ipywidgets` to avoid platform-specific dependencies.
*   The notebook environment is assumed to support `ipywidgets` for full interactivity. A fallback static visualization (saved PNG) will be provided for environments where interactivity might be limited.

### 4.3 Customization Instructions

*   **Risk Scenarios:** Users can define custom inherent risks and controls using the provided input fields, allowing them to simulate specific scenarios relevant to their interests.
*   **Synthetic Data Parameters:** Users can adjust parameters for synthetic data generation (e.g., number of events, date range, average loss amount) to explore different scales of simulated operational risk.
*   **Visualization Settings:** Users will be able to modify plot titles, axis labels, and colors where interactive controls are provided.
*   **Residual Risk Logic:** The notebook will allow users to switch between the "Simple" and "Weighted" residual risk calculation approaches as per the PRMIA Handbook.

### 4.4 User Interaction Guidelines

*   **Parameters:** Sliders, dropdowns, and text inputs will be provided for all customizable settings.
*   **Inline Help:** Each control will have inline help text or tooltips to describe its purpose and impact on the analysis. This can be achieved using `ipywidgets.HTML` or `Label` elements adjacent to controls.
*   **Clear Prompts:** Input cells will be preceded by clear markdown instructions and prompts for user interaction.

### 4.5 References

[1] PRMIA Operational Risk Manager Handbook, Published by PRMIA Publications, Wilmington, DE, Updated November, 2015. Document identifier: `PRMIA Operational Risk Manager Handbook.pdf`. This handbook provides a comprehensive overview of operational risk management, including the risk assessment lifecycle, taxonomies, and control assessment methodologies.

