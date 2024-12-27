import streamlit as st
import pickle

# Load the model
model_path = 'yurak_huruji.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Input fields for the model's features
age = st.number_input("Age", min_value=12, max_value=100, step=1, placeholder='Age', label_visibility="visible")
sex = st.number_input("Sex (0: Female, 1: Male)", min_value=0, max_value=1, step=1, placeholder='Sex', label_visibility="visible")
chest_pain_type = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"], index=0)
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, step=1, placeholder='RestingBP')
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=600, step=1, placeholder='Cholesterol')
fasting_bs = st.number_input("Fasting Blood Sugar > 120 mg/dL (0: No, 1: Yes)", min_value=0, max_value=1, step=1, placeholder='FastingBS')
resting_ecg = st.selectbox("Resting ECG", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"], index=0)
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, step=1, placeholder='MaxHR')
exercise_angina = st.selectbox("Exercise-Induced Angina (Yes/No)", options=["No", "Yes"], index=0)
oldpeak = st.number_input("Oldpeak (ST depression induced by exercise relative to rest)", min_value=0.0, max_value=10.0, step=0.1, placeholder='Oldpeak')
st_slope = st.selectbox("Slope of the peak exercise ST segment", options=["Upsloping", "Flat", "Downsloping"], index=0)

# Map categorical inputs to numerical values
chest_pain_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
resting_ecg_map = {"Normal": 0, "ST-T Wave Abnormality": 1, "Left Ventricular Hypertrophy": 2}
exercise_angina_map = {"No": 0, "Yes": 1}
st_slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}

# Prepare the feature vector for prediction
features = [
    age,
    sex,
    chest_pain_map[chest_pain_type],
    resting_bp,
    cholesterol,
    fasting_bs,
    resting_ecg_map[resting_ecg],
    max_hr,
    exercise_angina_map[exercise_angina],
    oldpeak,
    st_slope_map[st_slope]
]

# Make predictions
if st.button("Predict"):
    prediction = model.predict([features])
    prediction_proba = model.predict_proba([features])

    if prediction[0] == 1:
        st.error(f"High risk of heart attack! Confidence: {prediction_proba[0][1]*100:.2f}%")
    else:
        st.success(f"Low risk of heart attack! Confidence: {prediction_proba[0][0]*100:.2f}%")
