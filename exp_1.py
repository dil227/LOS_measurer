import streamlit as st

st.set_page_config(page_title="LOS Deviation Explorer", layout="centered")

st.title("Length of Stay Deviation Explorer")

def calc_delta(age, aki, sepsis, oxygen, delirium, placement,
               hb, platelets, inr, bilirubin, bun, creatinine, wbc,
               fever, sbp, hr, bmi):
    d = 0
    r = []

    if age > 80:
        d += 0.6
        r.append(("Age > 80", 0.6))
    elif age > 65:
        d += 0.3
        r.append(("Age > 65", 0.3))

    if aki == "Yes":
        d += 1.5
        r.append(("AKI", 1.5))
    if sepsis == "Yes":
        d += 2.0
        r.append(("Sepsis", 2.0))
    if oxygen == "Yes":
        d += 1.0
        r.append(("Oxygen needed", 1.0))
    if delirium == "Yes":
        d += 1.4
        r.append(("Delirium", 1.4))
    if placement == "Yes":
        d += 2.2
        r.append(("Placement issue", 2.2))

    if hb < 10:
        d += 0.7
        r.append(("Low Hb", 0.7))
    if platelets < 100:
        d += 0.8
        r.append(("Thrombocytopenia", 0.8))
    if inr > 1.5:
        d += 0.7
        r.append(("High INR", 0.7))
    if bilirubin > 2:
        d += 0.9
        r.append(("High bilirubin", 0.9))
    if bun > 30:
        d += 0.8
        r.append(("High BUN", 0.8))
    if creatinine > 2:
        d += 0.9
        r.append(("High creatinine", 0.9))
    if wbc > 15:
        d += 0.7
        r.append(("High WBC", 0.7))

    if fever == "Yes":
        d += 0.6
        r.append(("Fever", 0.6))
    if sbp < 100:
        d += 1.0
        r.append(("Low BP", 1.0))
    if hr > 100:
        d += 0.6
        r.append(("Tachycardia", 0.6))
    if bmi > 35:
        d += 0.3
        r.append(("BMI > 35", 0.3))

    return d, sorted(r, key=lambda x: x[1], reverse=True)


with st.form("los_form"):
    st.markdown("### Baseline")
    glos = st.number_input("gLOS (days)", min_value=0.0, max_value=30.0, value=4.5, step=0.1)
    hospital_los = st.number_input("Hospital LOS (days)", min_value=0.0, max_value=30.0, value=4.8, step=0.1)
    my_los = st.number_input("My LOS (days)", min_value=0.0, max_value=30.0, value=4.3, step=0.1)

    st.markdown("### Patient Factors")
    age = st.number_input("Age", min_value=18, max_value=120, value=68)
    aki = st.selectbox("AKI", ["No", "Yes"])
    sepsis = st.selectbox("Sepsis", ["No", "Yes"])
    oxygen = st.selectbox("Oxygen needed", ["No", "Yes"])
    delirium = st.selectbox("Delirium", ["No", "Yes"])
    placement = st.selectbox("Placement issue", ["No", "Yes"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=30.0, step=0.1)

    st.markdown("### Labs")
    hb = st.number_input("Hemoglobin", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
    platelets = st.number_input("Platelets", min_value=0, max_value=1000, value=250, step=1)
    inr = st.number_input("INR", min_value=0.5, max_value=10.0, value=1.1, step=0.1)
    bilirubin = st.number_input("Bilirubin", min_value=0.0, max_value=20.0, value=0.8, step=0.1)
    bun = st.number_input("BUN", min_value=0.0, max_value=200.0, value=18.0, step=1.0)
    creatinine = st.number_input("Creatinine", min_value=0.1, max_value=15.0, value=1.2, step=0.1)
    wbc = st.number_input("WBC", min_value=0.1, max_value=60.0, value=9.5, step=0.1)

    st.markdown("### Vitals")
    fever = st.selectbox("Fever", ["No", "Yes"])
    sbp = st.number_input("Systolic BP", min_value=50, max_value=250, value=120, step=1)
    hr = st.number_input("Heart Rate", min_value=30, max_value=200, value=80, step=1)

    submitted = st.form_submit_button("Calculate")


if submitted:
    delta, reasons = calc_delta(
        age, aki, sepsis, oxygen, delirium, placement,
        hb, platelets, inr, bilirubin, bun, creatinine, wbc,
        fever, sbp, hr, bmi
    )

    predicted = glos + delta
    vs_hospital = predicted - hospital_los
    vs_me = predicted - my_los

    st.metric("Predicted LOS", f"{predicted:.1f} days", f"{delta:+.1f} vs gLOS")

    if delta > 1.5:
        st.warning("Longer stay expected")
    elif delta > 0.5:
        st.info("Moderate increase")
    else:
        st.success("Near expected")

    st.markdown("### Comparison")
    st.write(f"Vs hospital LOS: {vs_hospital:+.1f} days")
    st.write(f"Vs my LOS: {vs_me:+.1f} days")

    st.markdown("### Top Drivers")
    if reasons:
        for name, val in reasons[:5]:
            st.write(f"- {name}: +{val:.1f}")
    else:
        st.write("No major prolonging factors selected.")