# California House Price Prediction

This project predicts house prices in California using the **California Housing Dataset**.  
It includes data loading, preprocessing, model training, evaluation, and visualization.

## 📌 Dataset
The dataset is fetched from **Scikit-Learn’s inbuilt `fetch_california_housing()`**.

## 📘 Features Used
- MedInc – Median Income  
- HouseAge – Average House Age  
- AveRooms – Average Rooms  
- AveBedrms – Average Bedrooms  
- Population  
- AveOccup – Average Occupancy  
- Latitude  
- Longitude  

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-Learn  

## 📊 Models Used
- Linear Regression  
- Decision Tree Regressor *(optional)*  
- Random Forest Regressor *(optional)*  

## 📈 Steps Covered
1. Load the California dataset  
2. Convert into DataFrame  
3. Split into train & test  
4. Train ML model  
5. Predict prices  
6. Evaluate using RMSE  

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py
