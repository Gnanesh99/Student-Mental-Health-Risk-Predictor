🧠 Student Mental Health Risk Predictor

This project uses machine learning to predict the risk of depression among students based on behavioral and demographic factors. It aims to support early identification of mental health risks using simple inputs.

🚀 Features

Predicts depression risk (Low / High)

Uses lifestyle-based inputs instead of direct clinical questions

Interactive web app built with Streamlit

Clean and simple user interface

🛠️ Tech Stack

Python

Pandas

Scikit-learn

Streamlit

Joblib

📊 Model Details

Algorithm: Logistic Regression

Dataset: Student Mental Health Survey

Features used:

Gender

Age

Marital Status

Anxiety (derived)

Panic Attack (derived)

Specialist Treatment

🧩 How It Works

User answers simple questions

Responses are converted into model features

Model predicts depression risk

Result is displayed instantly

💻 Run Locally
pip install -r requirements.txt
streamlit run app.py
🌐 Live Demo

(Your Streamlit link here)

📁 Project Structure
student-mental-health-risk-predictor
│
├── app.py
├── depression_model.pkl
├── mental_health_project.ipynb
├── dataset.csv
├── requirements.txt
└── README.md
🎯 Purpose

This project demonstrates how data science can be applied to real-world problems like student mental health and early risk detection.

⚠️ Disclaimer

This is not a medical tool. It is for educational and demonstration purposes only.
