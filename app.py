
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ----------------------------
# PAGE CONFIGURATION
# ----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="❤️",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}
.stButton > button {
    width: 100%;
    background-color: #1C3FAA;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}
h1, h2, h3 {
    color: #1C3FAA;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD MODEL
# ----------------------------
working_dir = os.getcwd()
model_path = os.path.join(
    working_dir,
    "saved model",
    "heart_disease_model.sav"
)
heart_disease_model = pickle.load(open(model_path, "rb"))

# ----------------------------
# SIDEBAR MENU
# ----------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Healthcare AI",
        options=[
            "Home",
            "Heart Disease Prediction",
            "About"
        ],
        icons=[
            "house",
            "heart",
            "info-circle"
        ],
        menu_icon="hospital-fill",
        default_index=0
    )

# ----------------------------
# HOME PAGE
# ----------------------------
if selected == "Home":
    st.title("❤️ Heart Disease Prediction System")
    st.markdown("""
    ### AI-Powered Cardiovascular Risk Assessment
    This application uses Machine Learning to assess
    the likelihood of heart disease based on medical indicators.
    Enter patient information and receive an instant prediction.
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Model Accuracy",
            value="91%"
        )
    with col2:
        st.metric(
            label="Precision",
            value="89%"
        )
    with col3:
        st.metric(
            label="Recall",
            value="88%"
        )

# ----------------------------
# HEART DISEASE PREDICTION PAGE
# ----------------------------
elif selected == "Heart Disease Prediction":
    st.title("❤️ Heart Disease Prediction")
    st.subheader("Enter Patient Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=40
        )
        trestbps = st.number_input(
            "Resting Blood Pressure",
            value=120
        )
        restecg = st.number_input(
            "Resting ECG Results",
            value=0
        )
        oldpeak = st.number_input(
            "ST Depression",
            value=0.0
        )
        thal = st.number_input(
            "Thal",
            value=1
        )
    with col2:
        sex = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )
        chol = st.number_input(
            "Serum Cholesterol (mg/dl)",
            value=200
        )
        thalach = st.number_input(
            "Maximum Heart Rate Achieved",
            value=150
        )
        slope = st.number_input(
            "Slope",
            value=1
        )
    with col3:
        cp = st.number_input(
            "Chest Pain Type",
            value=0
        )
        fbs = st.number_input(
            "Fasting Blood Sugar",
            value=0
        )
        exang = st.number_input(
            "Exercise Induced Angina",
            value=0
        )
        ca = st.number_input(
            "Major Vessels Colored by Fluoroscopy",
            value=0
        )
    # Convert gender to numeric
    sex_value = 1 if sex == "Male" else 0
    # Prediction Button
    if st.button("Predict Heart Disease"):
        input_data = [[
            age,
            sex_value,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]]
        prediction = heart_disease_model.predict(input_data)
        st.subheader("Prediction Result")
        if prediction[0] == 1:
            st.error("""
            🔴 HIGH RISK DETECTED
            The model predicts a higher likelihood
            of heart disease.
            Please consult a qualified healthcare professional.
            """)
        else:
            st.success("""
            🟢 LOW RISK DETECTED
            The model predicts a lower likelihood
            of heart disease.
            Maintain a healthy lifestyle and
            continue regular medical checkups.
            """)

# ----------------------------
# ABOUT PAGE
# ----------------------------
elif selected == "About":
    st.title("About This Application")
    st.markdown("""
    ### Heart Disease Prediction System
    This application leverages Machine Learning algorithms
    to predict the likelihood of heart disease based on
    patient health indicators.
    #### Features
    - Real-time prediction
    - User-friendly interface
    - Fast and accurate assessment
    - Responsive design
    #### Disclaimer
    This application is intended for educational and
    research purposes only and should not be used as a
    substitute for professional medical diagnosis.
    """)
    st.info(
        "Developed using Python, Streamlit, and Scikit-Learn."
    )
