# 💼 Employee Salary Prediction System

A simple yet powerful **Machine Learning web app** built with **Streamlit** that predicts an employee's expected salary based on their **country**, **education level**, and **professional coding experience**.

<br/>

## 🚀 Features

- 🎓 Predict salary based on educational qualifications  
- 🌍 Country-wise salary trends  
- 🧠 ML model using Decision Tree Regressor  
- 🔒 Encoded & cleaned dataset with preprocessing  
- ⚡ Fast, lightweight Streamlit frontend  

<br/>

## 📸 App Demo

![App Screenshot](https://github.com/harshita-89/Employee_Salary_prediction/blob/main/images/Salary_pred_webApp.jpg?raw=true)

<br/>

## 🧠 How It Works

1. Load a trained model and label encoders from a `.pkl` file  
2. Accept user input for:
   - Country  
   - Education Level  
   - Years of Experience  
3. Predict annual salary using the trained model  
4. Display estimated salary in a user-friendly UI  

<br/>

## 📂 Project Structure
Employee Salary Prediction System/

├── app.py # Streamlit frontend

├── model_training.ipynb # Colab notebook to clean data & train model

├── SalaryPredModel.pkl # Saved ML model & encoders

├── requirements.txt # Project dependencies

├── images/ # Screenshot for demo

│ └── Salary_pred_webApp.jpg

├── .gitignore

└── README.md # You're reading this!


<br/>

## 🔧 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/employee-salary-prediction.git
cd employee-salary-prediction
### 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate      (On Windows)
source venv/bin/activate   (On macOS/Linux)
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Run the App
streamlit run app.py
Then open http://localhost:8501 in your browser.

<br/>
📦 Dependencies
Main packages used:

- streamlit

- scikit-learn

- numpy

- pandas

- pickle (standard library)

- See full list in requirements.txt

<br/>

📊 Model Details

- Algorithm: Decision Tree Regressor

- Trained On: StackoverflowSurvey

- Target: ConvertedCompYearly (Annual salary)

<br/>

📃 License
This project is licensed under the MIT License.

Made with ❤️ using Python, Streamlit, and Coffee.
