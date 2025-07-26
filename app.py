import streamlit as st
import pickle
import pandas as pd

# Load saved model and encoders
with open("SalaryPredModel.pkl", "rb") as file:
    data = pickle.load(file)

model = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Define UI options
country_list = le_country.classes_
education_list = le_education.classes_

# Streamlit App UI
st.set_page_config(page_title="Salary Prediction App", layout="centered")
st.title("💼 Salary Prediction App")
st.markdown("#### Estimate a developer's expected salary based on your profile")

# Input
st.write("### Enter Your Details:")
col1, col2 = st.columns(2)

with col1:
    country = st.selectbox("🌍 Country", country_list)

with col2:
    education = st.selectbox("🎓 Education Level", education_list)

experience = st.slider("💼 Years of Professional Coding Experience", 0, 50, 1)

# Predict
if st.button("Predict Salary"):
    input_df = pd.DataFrame([[country, education, experience]],
                            columns=["Country", "EdLevel", "YearsCodePro"])
    
    input_df["Country"] = le_country.transform(input_df["Country"])
    input_df["EdLevel"] = le_education.transform(input_df["EdLevel"])

    salary = model.predict(input_df)[0]
    st.success(f"💰 Estimated Salary: **${salary:,.2f} USD per year**")
    st.markdown("💡 *Note: This is an estimated average based on global survey data.*")
