import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("Process.pkl", "rb"))

st.set_page_config(page_title="AI Procurement Strategy Engine By Vinay", layout="centered")

st.title("📊 AI Procurement Strategy Engine")
st.write("Predict Kraljic Category using ML Model")

st.divider()

# Input Fields
lead_time = st.number_input("Lead Time (Days)", min_value=0)
order_volume = st.number_input("Order Volume (Units)", min_value=0)
cost_per_unit = st.number_input("Cost per Unit")
supply_risk = st.slider("Supply Risk Score", 0.0, 10.0)
profit_impact = st.slider("Profit Impact Score", 0.0, 10.0)
environmental_impact = st.slider("Environmental Impact", 0.0, 10.0)
single_source_risk = st.selectbox("Single Source Risk", [0, 1])

st.divider()

if st.button("Predict Kraljic Category"):

    features = np.array([[lead_time,
                          order_volume,
                          cost_per_unit,
                          supply_risk,
                          profit_impact,
                          environmental_impact,
                          single_source_risk]])

    prediction = model.predict(features)[0]

    st.success(f"Predicted Category: {prediction}")

    # Strategy Recommendation
    if prediction == "Strategic":
        st.info("🔵 Strategy: Build long-term partnerships & secure supply contracts.")
    elif prediction == "Leverage":
        st.info("🟢 Strategy: Negotiate better pricing & bulk discounts.")
    elif prediction == "Bottleneck":
        st.info("🟡 Strategy: Reduce supply risk & identify alternative suppliers.")
    elif prediction == "Non-Critical":
        st.info("⚪ Strategy: Automate procurement & simplify ordering process.")
