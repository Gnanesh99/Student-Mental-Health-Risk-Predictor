import streamlit as st
import joblib
import pandas as pd

# load model
model = joblib.load("depression_model.pkl")

st.title("Student Mental Health Risk Predictor")

# inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 16, 40)

marital = st.selectbox("Marital Status", ["No", "Yes"])

overthinking = st.selectbox("Do you overthink often?", ["Never", "Sometimes", "Often"])
nervousness = st.selectbox("Do you often feel nervous or restless?", ["No", "Yes"])
sudden_fear = st.selectbox("Do you experience sudden intense fear?", ["No", "Yes"])

specialist = st.selectbox("Have you consulted a mental health specialist?", ["No", "Yes"])


# convert inputs
gender = 1 if gender == "Female" else 0
marital = 1 if marital == "Yes" else 0
treatment = 1 if specialist == "Yes" else 0

if overthinking == "Often" or nervousness == "Yes":
    anxiety = 1
else:
    anxiety = 0

panic_attack = 1 if sudden_fear == "Yes" else 0


# prediction
if st.button("Predict Risk"):

    input_data = pd.DataFrame([[gender, age, marital, anxiety, panic_attack, treatment]],
    columns=[
        "Choose your gender",
        "Age",
        "Marital status",
        "Do you have Anxiety?",
        "Do you have Panic attack?",
        "Did you seek any specialist for a treatment?"
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Depression")
    else:
        st.success("Low Risk of Depression")