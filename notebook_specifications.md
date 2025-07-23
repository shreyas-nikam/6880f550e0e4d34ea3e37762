
# Technical Specification for Jupyter Notebook: Operational Loss Event Analyzer (Basel Taxonomy)

## 1. Notebook Overview

### 1.1 Learning Goals

This Jupyter Notebook is designed to provide users with a practical understanding of operational risk analysis using the Basel taxonomy. Upon completion, users will be able to:

*   **Understand Operational Risk Categorization**: Comprehend the seven official Basel defined event types for operational loss events, as outlined in the PRMIA Operational Risk Manager Handbook [1, page 15].
*   **Identify Trends and Patterns**: Learn to identify temporal trends and patterns in simulated operational loss data.
*   **Explore Relationships and Impact**: Analyze correlations between different event types, their financial impact, and frequency.
*   **Appreciate Data-Driven Risk Management**: Understand the importance of collecting, structuring, and analyzing operational risk data for effective risk management.
*   **Grasp Risk Assessment Concepts**: Gain insights into fundamental risk concepts such as Inherent Risk, Control Effectiveness, and Residual Risk, including their conceptual relationships and practical mapping.

### 1.2 Expected Outcomes

By interacting with this notebook, users will achieve the following:

*   **Synthetic Data Generation**: Successfully generate and prepare a realistic synthetic dataset of operational loss events.
*   **Data Validation and Exploration**: Perform basic data validation, cleaning, and generate descriptive statistics for the simulated loss events.
*   **Interactive Data Filtering**: Utilize interactive widgets to dynamically filter and focus on specific subsets of the loss event data based on various criteria.
*   **Visual Insights**: Generate a series of professional-quality visualizations (trend, aggregated comparison, and relationship plots) that reveal key insights into operational loss events.
*   **Conceptual Understanding**: Solidify their understanding of how operational risk data can be structured and analyzed to inform risk management decisions, particularly in the context of Basel II.

## 2. Mathematical and Theoretical Foundations

This section will introduce the core concepts of operational risk as defined by the Basel Accords, emphasizing the importance of a structured taxonomy and data-driven analysis.

### 2.1 Operational Risk Definition

Operational risk is defined by Basel II as:
$$ \text{Operational Risk} = \text{The risk of loss resulting from inadequate or failed internal processes, people, and systems, or from external events.} $$
This definition includes legal risk but explicitly excludes strategic and reputational risk [1, page 13]. It highlights that "Operational risk is a data-driven discipline, and relies on development and maintenance of well-constructed hierarchies that allow for aggregation and analysis of loss trends" [1, page 16].

### 2.2 Basel Event Types

The Basel Committee on Banking Supervision (BCBS) has defined seven official categories for operational loss events, providing a standardized taxonomy for risk reporting and analysis. These categories are crucial for consistent data collection and comparative analysis across institutions. The seven event types are [1, page 15-16]:

1.  **Internal Fraud**: Losses due to acts intended to defraud, misappropriate property, or circumvent regulations, law, or company policy, involving at least one internal party.
2.  **External Fraud**: Losses due to acts intended to defraud, misappropriate property, or circumvent the law by a third party.
3.  **Employment Practices and Workplace Safety**: Losses arising from acts inconsistent with employment, health or safety laws or agreements, or from payment of personal injury claims or diversity/discrimination events.
4.  **Clients, Products, and Business Practices**: Losses arising from an unintentional or negligent failure to meet a professional obligation to specific clients or from the nature/design of a product.
5.  **Damage to Physical Assets**: Losses arising from loss or damage to physical assets from natural disasters or other events.
6.  **Business Disruption and System Failures**: Losses arising from disruption of business or system failures (e.g., IT systems, hardware, software, telecommunications).
7.  **Execution, Delivery, and Process Management**: Losses from failed transaction processing or process management, relations with trade counterparties and vendors, data entry errors, etc.

### 2.3 Risk Assessment Concepts

Understanding operational risk involves assessing various risk components:

*   **Inherent Risk (IR)**: This is the level of risk before any controls or mitigation strategies are applied. It is often described as "risk without controls" [1, page 37]. It represents the raw risk exposure of an activity or process.
*   **Control Effectiveness (CE)**: This refers to how well the existing controls are designed and implemented to mitigate the inherent risks. Controls can be preventative (preventing an event from occurring) or detective (detecting an event after it occurs) [1, page 33].
*   **Residual Risk (RR)**: This is the risk that remains after controls have been implemented and are operating. Conceptually, it can be thought of as:
    $$ \text{Residual Risk} = \text{Inherent Risk} - \text{Impact of Controls} $$
    However, the PRMIA Handbook explicitly states that this is "not a subtractive exercise" [1, page 38]. Instead, residual risk is typically determined through a qualitative mapping or rating scale that combines Inherent Risk and Control Effectiveness ratings. The notebook will adopt this matrix-based approach for determining residual risk, which is a common practice in operational risk management.

    For this lab, we will use the following qualitative mapping, adapted from the PRMIA Handbook [1, page 38]:

    **Residual Risk Chart (Standard Approach)**
    | Inherent Risk   | Control Effectiveness: Effective | Control Effectiveness: Partially Effective | Control Effectiveness: Ineffective |
    |:----------------|:---------------------------------|:-----------------------------------------|:---------------------------------|
    | High            | Low                              | Medium                                   | High                             |
    | Medium          | Low                              | Medium                                   | Medium                           |
    | Low             | Low                              | Low                                      | Low                              |

    **Residual Risk Chart (Weighted Approach for High Legal/Regulatory Risks)**
    *This approach applies additional weighting to control deficiencies, leading to potentially higher residual risk ratings, especially when violations of law are a concern.*
    | Inherent Risk   | Control Effectiveness: Effective | Control Effectiveness: Partially Effective | Control Effectiveness: Ineffective |
    |:----------------|:---------------------------------|:-----------------------------------------|:---------------------------------|
    | High            | Low                              | Medium                                   | High                             |
    | Medium          | Low                              | Medium                                   | High                             |
    | Low             | Low                              | Low                                      | Medium                           |

    The notebook will illustrate how this mapping allows for a more nuanced understanding of remaining risk, acknowledging that even low inherent risks can become significant residual risks if controls are ineffective, particularly in highly regulated areas.

## 3. Code Requirements

This section outlines the logical flow, necessary libraries, input/output, and algorithms for the Jupyter Notebook.

### 3.1 Logical Flow

The notebook will follow a clear, step-by-step logical flow:

1.  **Introduction and Setup**:
    *   Markdown cell: Welcome and brief overview of the notebook's purpose.
    *   Code cell: Import necessary libraries.
    *   Code cell: Define global parameters (e.g., number of synthetic records, date range for generation).
2.  **Synthetic Data Generation**:
    *   Markdown cell: Explain the need for synthetic data and its characteristics.
    *   Code cell: Implement a function to generate synthetic operational loss data.
    *   Code cell: Call the generation function and display the first few rows and basic info.
3.  **Data Validation and Preprocessing**:
    *   Markdown cell: Describe the importance of data validation.
    *   Code cell: Implement data validation checks (column names, types, missing values, uniqueness).
    *   Code cell: Perform any necessary data type conversions (e.g., 'Date' to datetime, 'Loss_Amount' to numeric).
    *   Code cell: Display summary statistics for key numeric columns.
4.  **Interactive Filtering and Analysis Setup**:
    *   Markdown cell: Introduce interactive filtering to allow users to explore subsets of data.
    *   Code cell: Set up interactive widgets (dropdowns for `Basel_Event_Type`, sliders for `Date_Range` and `Loss_Amount_Range`).
    *   Code cell: Define a function that applies filters based on widget selections and updates the analysis.
5.  **Data Analysis and Visualization**:
    *   Markdown cell: Explain the types of insights each visualization aims to provide.
    *   Code cell: Implement functions for each core visualization.
    *   Code cell: Display the interactive analysis output, including plots and summary statistics, driven by the filtering function.
6.  **Summary of Findings and Conclusion**:
    *   Markdown cell: Discuss key insights derived from the analysis.
    *   Markdown cell: Concluding remarks and next steps.
7.  **References**:
    *   Markdown cell: List all external datasets or libraries used, crediting the PRMIA Handbook.

### 3.2 Expected Libraries

Only open-source Python libraries from PyPI will be used.

*   **`pandas`**: For data manipulation, DataFrame operations, and data loading/saving.
*   **`numpy`**: For numerical operations, especially in synthetic data generation.
*   **`faker`**: For generating realistic synthetic categorical and text data.
*   **`matplotlib.pyplot`**: For static plotting.
*   **`seaborn`**: For enhanced statistical visualizations, built on Matplotlib.
*   **`plotly.express` / `plotly.graph_objects`**: For interactive visualizations (preferred). A static fallback will be provided.
*   **`ipywidgets`**: For creating interactive user controls like dropdowns and sliders.

### 3.3 Input/Output Expectations

*   **Input**:
    *   The primary input will be a **synthetic dataset** generated programmatically within the notebook. This ensures self-containment and reproducibility.
    *   The `generate_synthetic_loss_data` function will accept parameters (e.g., `num_records`) to control the dataset size.
    *   **Optional Sample Data**: A lightweight sample dataset (e.g., a small CSV or JSON file, ≤ 5 MB) will be provided as an optional input. This allows the notebook to run without re-generating data, serving as a static fallback or for quick demonstrations.
*   **Output**:
    *   **Validated DataFrame**: A `pandas.DataFrame` object after validation and cleaning steps.
    *   **Summary Statistics**: Tables or print statements displaying total loss, average loss per event type, event counts, and basic descriptive statistics for numeric fields.
    *   **Visualizations**:
        *   Interactive plots (if `ipywidgets` and `plotly` are supported in the user's environment).
        *   Static image files (e.g., PNG) generated and saved for each plot, serving as a fallback for environments where interactivity is not supported.
    *   **Console Output**: Informative messages, validation logs, and progress updates.

### 3.4 Algorithms or Functions to be Implemented (without code)

1.  **`generate_synthetic_loss_data(num_records)`**
    *   **Purpose**: Creates a `pandas.DataFrame` representing synthetic operational loss events.
    *   **Input**: `num_records` (integer, number of rows to generate).
    *   **Output**: `pandas.DataFrame` with columns:
        *   `Event_ID`: Unique identifier (e.g., UUID or sequential integer).
        *   `Date`: Time-series data (random dates within a specified range).
        *   `Basel_Event_Type`: Categorical, from the 7 Basel types (e.g., "Internal Fraud", "System Failure").
        *   `Loss_Amount`: Numeric, representing financial impact (e.g., float, potentially skewed distribution).
        *   `Impact_Category`: Categorical (e.g., "Financial", "Reputational", "Regulatory").
        *   `Contributing_Factors`: Text/categorical (brief descriptions or categories of contributing factors).
    *   **Implementation Note**: Use `numpy.random` for numeric distributions, `pandas` for date ranges, and `faker` for more diverse categorical/text entries. Ensure realistic distributions for `Loss_Amount` and `Date`.

2.  **`validate_data(df)`**
    *   **Purpose**: Confirms data integrity and readiness for analysis.
    *   **Input**: `df` (pandas DataFrame).
    *   **Output**: Boolean (True if valid, False otherwise) and prints validation results/warnings.
    *   **Checks**:
        *   Expected column names presence.
        *   Correct data types for key columns (`Date` as datetime, `Loss_Amount` as numeric).
        *   Uniqueness of `Event_ID` as primary key.
        *   Absence of missing values in critical fields (`Event_ID`, `Date`, `Basel_Event_Type`, `Loss_Amount`).
        *   Log summary statistics for numeric columns (mean, median, standard deviation).

3.  **`filter_data(df, event_type=None, date_range=None, loss_amount_range=None)`**
    *   **Purpose**: Filters the DataFrame based on user selections from interactive widgets.
    *   **Input**:
        *   `df` (pandas DataFrame).
        *   `event_type` (list of strings or `None`).
        *   `date_range` (tuple of datetime or `None`).
        *   `loss_amount_range` (tuple of (min, max) float or `None`).
    *   **Output**: Filtered `pandas.DataFrame`.

4.  **`calculate_summary_statistics(df)`**
    *   **Purpose**: Computes key statistical measures for the filtered data.
    *   **Input**: `df` (pandas DataFrame).
    *   **Output**: Dictionary or DataFrame containing:
        *   Total `Loss_Amount`.
        *   Average `Loss_Amount` per event.
        *   Event count per `Basel_Event_Type`.
        *   Average `Loss_Amount` per `Basel_Event_Type`.

5.  **`plot_trend(df, title, x_label, y_label)`**
    *   **Purpose**: Visualizes loss trends over time.
    *   **Input**: `df` (filtered DataFrame), plot metadata.
    *   **Output**: A line or area chart showing `Loss_Amount` over time, segmented by `Basel_Event_Type`.
    *   **Visualization Details**:
        *   X-axis: `Date` (aggregated by month/quarter/year).
        *   Y-axis: Sum of `Loss_Amount`.
        *   Lines/Areas: Different colors for each `Basel_Event_Type`.
        *   Interactive features (zoom, pan, hover tooltips) if using `plotly`.
        *   Static PNG fallback if interactivity is not available.

6.  **`plot_aggregated_comparison(df, title, x_label, y_label)`**
    *   **Purpose**: Compares total or average loss across categorical dimensions.
    *   **Input**: `df` (filtered DataFrame), plot metadata.
    *   **Output**:
        *   **Option 1 (Bar Chart)**: A bar chart showing total `Loss_Amount` per `Basel_Event_Type`.
            *   X-axis: `Basel_Event_Type`.
            *   Y-axis: Total `Loss_Amount`.
            *   Bars: Ordered by `Loss_Amount` (descending).
        *   **Option 2 (Heatmap)**: A heatmap showing `Loss_Amount` by `Basel_Event_Type` and `Impact_Category`.
            *   Rows: `Basel_Event_Type`.
            *   Columns: `Impact_Category`.
            *   Color intensity: Represents aggregated `Loss_Amount`.
    *   **Visualization Details**: Clear labels, legends, and color-blind friendly palette. Static PNG fallback.

7.  **`plot_relationship(df, title, x_label, y_label)`**
    *   **Purpose**: Explores the relationship between `Loss_Amount` and event frequency.
    *   **Input**: `df` (filtered DataFrame), plot metadata.
    *   **Output**: A scatter plot.
    *   **Visualization Details**:
        *   X-axis: `Frequency` (e.g., number of events within a period or per type).
        *   Y-axis: `Loss_Amount` (e.g., average or max).
        *   Points: Colored by `Impact_Category`.
        *   Reveals clusters of high-frequency/low-impact vs. low-frequency/high-impact events.
        *   Clear labels, legends, and color-blind friendly palette. Static PNG fallback.

8.  **`create_interactive_filters(df)`**
    *   **Purpose**: Sets up and displays `ipywidgets` for user interaction.
    *   **Input**: `df` (initial DataFrame to determine filter options).
    *   **Output**: Interactive controls (dropdowns, sliders) linked to the `filter_data` and plotting functions, triggering updates upon user input.
    *   **Details**:
        *   Dropdown for `Basel_Event_Type` (multi-select allowed).
        *   Date range slider/selector for `Date`.
        *   Numeric range slider for `Loss_Amount`.
        *   Inline help text/tooltips for each control.

### 3.5 Markdown Explanations and Code Comments

Each major step in the notebook will include:

*   **Narrative Cells (Markdown)**: Brief explanations of *what* is being done in the subsequent code cell(s) and *why* it is important for the analysis.
*   **Code Comments**: Inline comments within code cells to explain specific lines or blocks of code.

## 4. Additional Notes or Instructions

### 4.1 Assumptions

*   The user has a basic understanding of Python and Jupyter notebooks.
*   The generated synthetic data, while realistic in its structure, is sufficient for demonstrating the concepts and analytical techniques.
*   The Basel Taxonomy (7 event types) from the PRMIA Handbook is the primary classification system for operational loss events.

### 4.2 Constraints

*   **Execution Environment**: The notebook must execute end-to-end on a mid-spec laptop (8 GB RAM).
*   **Performance**: Total execution time for the entire notebook should be under 5 minutes.
*   **Libraries**: Only open-source Python libraries available on PyPI may be used. No proprietary or non-standard libraries are permitted.
*   **No Code Implementation**: Python code itself should not be written in this specification document. Only descriptions of functions and algorithms are required.
*   **No Deployment Steps**: The specification should not include any details related to deployment or specific platform integration (e.g., Streamlit, Dash).

### 4.3 Customization Instructions

*   **Synthetic Data Parameters**: Users should be able to easily modify parameters for synthetic data generation (e.g., number of records, date range for events, distribution characteristics for loss amounts) at the beginning of the notebook.
*   **Interactive Analysis Settings**: The `ipywidgets` will provide interactive controls (sliders, dropdowns) for users to filter the data by `Basel_Event_Type`, `Date_Range`, and `Loss_Amount_Range`. These controls will allow learners to rerun analyses with different settings.
*   **Plotting Style**: The notebook will adopt a color-blind-friendly palette. All plots must include clear titles, labeled axes, and legends. Font size for all plot elements should be equal to or greater than 12pt.
*   **Inline Help**: Inline help text or tooltips will be provided for all interactive controls to describe their functionality.
*   **Static Fallback**: For environments that do not fully support interactive plotting libraries, a mechanism to save static PNG images of all core visualizations will be included.

### 4.4 References

*   **[1] PRMIA Operational Risk Manager Handbook**, Published by PRMIA Publications, Wilmington, DE, Updated November, 2015. Document identifier: `PRMIA Operational Risk Manager Handbook.pdf`. This handbook defines operational risk and outlines the seven official Basel defined event types, and discusses risk assessment methodologies.
*   **Python Libraries**: `pandas`, `numpy`, `faker`, `matplotlib`, `seaborn`, `plotly`, `ipywidgets`.
