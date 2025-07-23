
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the Operational Risk Assessment Lifecycle Simulator. This application provides an interactive simulation of the operational risk assessment lifecycle within a financial institution, as described in the "PRMIA Operational Risk Manager Handbook".

**Key Learning Outcomes:**
*   Understand the key stages and flow of a robust operational risk assessment program.
*   Learn how top-down risk identification informs bottom-up control assessment.
*   Explore the interplay between inherent risk, control effectiveness, and residual risk.
*   Recognize the importance of clear taxonomies and consistent tracking in risk management.
""")
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Loss Data Simulation", "Risk Assessment"])
if page == "Overview":
    from application_pages.overview import run_overview
    run_overview()
elif page == "Loss Data Simulation":
    from application_pages.loss_data_simulation import run_loss_data_simulation
    run_loss_data_simulation()
elif page == "Risk Assessment":
    from application_pages.risk_assessment import run_risk_assessment
    run_risk_assessment()
# Your code ends
