# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview  
This project builds a **Machine Learning model** to predict the **selling price of used cars** based on various features such as car age, fuel type, transmission type, and kilometers driven. It utilizes **Linear Regression** and **Lasso Regression** to train predictive models and evaluates their performance using **R-squared error**.  

---

## 📊 Dataset  
The dataset used in this project is `car data.csv`, which contains information about:  
- **Car Name** (Dropped for modeling)  
- **Year** (Manufacturing year)  
- **Present Price** (Current market price of the car)  
- **Kms Driven** (Total kilometers driven)  
- **Fuel Type** (Petrol, Diesel, CNG)  
- **Seller Type** (Dealer, Individual)  
- **Transmission** (Manual, Automatic)  
- **Owner** (Number of previous owners)  
- **Selling Price** (Target variable)  

---

## 🚀 Technologies Used  
- **Python** (Data Processing & Model Training)  
- **Pandas** (Data Manipulation)  
- **Matplotlib & Seaborn** (Data Visualization)  
- **Scikit-Learn** (Machine Learning)  
- **Joblib** (Model Serialization)  

---

## 🔍 Data Preprocessing  
1. **Loading & Cleaning the Dataset**  
   - Checking for null values and data types.  
   - Dropping unnecessary columns (`Car_Name`).  
2. **Encoding Categorical Variables**  
   - `Fuel_Type`, `Seller_Type`, and `Transmission` are converted to numerical values.  
3. **Splitting the Data**  
   - Features (`X`) and Target (`Y`) are separated.  
   - Data is split into **90% training** and **10% testing**.  

---

## 📈 Model Training & Evaluation  
### 🔹 **Linear Regression**  
- Model is trained using `LinearRegression()` from Scikit-Learn.  
- Performance is evaluated using **R-squared error**.  

### 🔹 **Lasso Regression**  
- Implemented using `Lasso()` for feature selection and reducing overfitting.  
- Performance is compared with Linear Regression.  

### 📊 **Model Performance**  
The models' accuracy is evaluated by comparing **actual vs. predicted prices** using **scatter plots**.  

---

## 🛠 Model Deployment  
- Trained models are saved using `joblib.dump()`.  
- Function `predict_price()` is implemented for **real-time car price prediction** based on user inputs.  
- Example Prediction:  
   ```python
   predicted_price = predict_price(2015, 5.5, 50000, "Diesel", "Dealer", "Manual", 0, model="linear")
   print(f"Predicted Selling Price: ₹{predicted_price:.2f} Lakhs")
