# Insurance Charges Prediction App

This is a Streamlit-based Machine Learning web application that predicts **insurance charges** using **Linear Regression**. Users can upload their own insurance dataset (CSV), clean missing data, train the model, and generate predictions. The app also displays a **radar chart** comparing user input with dataset feature ranges.

## 🚀 Features
- Upload insurance CSV dataset  
- Automatic handling of missing values (mean/mode imputation)  
- Label Encoding for categorical columns  
- Train Linear Regression model  
- Display model performance (MSE)  
- Predict insurance charges from user input  
- Radar chart visualization using Plotly  
- User-friendly Streamlit interface  

## 📂 Dataset Requirements
Your CSV must contain these columns:  
`age`, `bmi`, `children`, `smoker` (yes/no), `region`, `charges`

## 🛠️ Technologies Used
- Python  
- Streamlit  
- Pandas, NumPy  
- Scikit-learn  
- Plotly  
- Seaborn, Matplotlib  

## ▶️ How to Run
1. Install dependencies:
 pip install streamlit pandas numpy scikit-learn plotly seaborn matplotlib


2. Run the app:
 streamlit run insurance_prediction_app.py


## 📊 Model Details
- Algorithm: Linear Regression  
- Missing values: SimpleImputer  
- Encoding: LabelEncoder (`smoker`, `region`)  
- Train/Test split: 80/20  
- Metric: Mean Squared Error (MSE)

## 🧩 Visualizations
- Dataset preview  
- Missing value summary  
- Radar chart  
  - User input  
  - Dataset minimum  
  - Dataset maximum  


## ⭐ Contributions
Feel free to fork, improve, or raise issues!
