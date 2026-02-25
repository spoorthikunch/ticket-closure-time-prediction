import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    return joblib.load("rf_pipeline.pkl")

model = load_model()

st.title("🎫 Ticket Closure Time Prediction")

st.write("Enter ticket details below:")

location = st.text_input("Location")
category = st.text_input("Category")
subcategory = st.text_input("Subcategory")
u_symptom = st.text_input("User Symptom")
assignment_group = st.text_input("Assignment Group")
assigned_to = st.text_input("Assigned To")

impact = st.selectbox("Impact", ["High", "Medium", "Low"])
urgency = st.selectbox("Urgency", ["High", "Medium", "Low"])
priority = st.selectbox("Priority", ["High", "Medium", "Low"])

reassignment_count = st.number_input("Reassignment Count", min_value=0)
opened_date = st.number_input("Opened Date (1-31)", 1, 31)
opened_month = st.number_input("Opened Month (1-12)", 1, 12)
opened_dayofweek = st.number_input("Opened Day of Week (0-6)", 0, 6)
opened_hour = st.number_input("Opened Hour (0-23)", 0, 23)

active = st.selectbox("Active", [0, 1])
knowledge = st.selectbox("Knowledge", [0, 1])
u_priority_confirmation = st.selectbox("Priority Confirmation", [0, 1])

if st.button("Predict"):

    input_df = pd.DataFrame({
        "location": [location],
        "category": [category],
        "subcategory": [subcategory],
        "u_symptom": [u_symptom],
        "impact": [impact],
        "urgency": [urgency],
        "priority": [priority],
        "assignment_group": [assignment_group],
        "assigned_to": [assigned_to],
        "reassignment_count": [reassignment_count],
        "opened_date": [opened_date],
        "opened_month": [opened_month],
        "opened_dayofweek": [opened_dayofweek],
        "opened_hour": [opened_hour],
        "active": [active],
        "knowledge": [knowledge],
        "u_priority_confirmation": [u_priority_confirmation]
    })

    prediction = model.predict(input_df)

    st.success(f"Predicted Closure Time: {prediction[0]:.2f} hours")