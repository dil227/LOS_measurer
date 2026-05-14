import streamlit as st
import streamlit as st

with st.container():

    st.markdown("## LOS Metrics")

    glos = st.number_input(
        "gLOS (days)",
        min_value=0.0,
        max_value=30.0,
        value=4.5,
        step=0.1
    )

    hospital_los = st.number_input(
        "Hospital LOS (days)",
        min_value=0.0,
        max_value=30.0,
        value=4.8,
        step=0.1
    )

    my_los = st.number_input(
        "My LOS (days)",
        min_value=0.0,
        max_value=30.0,
        value=4.3,
        step=0.1
    )

    st.markdown("## Patient Factors")

    age = st.number_input("Age", 18, 120, 68)

    aki = st.selectbox("AKI", ["No", "Yes"])
    sepsis = st.selectbox("Sepsis", ["No", "Yes"])
    oxygen = st.selectbox("Oxygen needed", ["No", "Yes"])
    delirium = st.selectbox("Delirium", ["No", "Yes"])
    placement = st.selectbox("Placement issue", ["No", "Yes"])

    st.write(f"AKI: " {aki}, "Sepsis: " {sepsis}, "Oxygen: " {oxygen}, "Delirium: " {delirium}, "Placement: " {placement})

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=30.0,
        step=0.1
    )

    st.markdown("## Labs")

    hb = st.number_input("Hemoglobin", 0.0, 20.0, 12.0, 0.1)
    platelets = st.number_input("Platelets", 0, 1000, 250)
    inr = st.number_input("INR", 0.5, 10.0, 1.1, 0.1)
    bilirubin = st.number_input("Bilirubin", 0.0, 20.0, 0.8, 0.1)
    bun = st.number_input("BUN", 0.0, 200.0, 18.0, 1.0)
    creatinine = st.number_input("Creatinine", 0.1, 15.0, 1.2, 0.1)
    wbc = st.number_input("WBC", 0.1, 60.0, 9.5, 0.1)

    st.markdown("## Vitals")

    fever = st.selectbox("Fever", ["No", "Yes"])

    bp = st.number_input(
        "Systolic BP",
        min_value=50,
        max_value=250,
        value=120,
        step=1
    )

    hr = st.number_input(
        "Heart Rate",
        min_value=30,
        max_value=200,
        value=80,
        step=1
    )

    st.write()




    