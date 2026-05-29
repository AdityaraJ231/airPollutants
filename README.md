Air Pollution Analysis & Prediction using Python

📌 Project Overview

This project focuses on Air Quality Index (AQI) Analysis and Prediction using Python.
The analysis was performed on real-time air pollution data collected from multiple cities and states in India.

The project includes:

Data Cleaning & Preprocessing
Exploratory Data Analysis (EDA)
Data Visualization
Outlier Detection & Removal
Normalization
Correlation Analysis
AQI Categorization
Machine Learning Prediction using Linear Regression

The goal of this project is to understand pollution trends and predict PM2.5 levels using other pollutant values.


📂 Dataset
Source: Government Open Data Platform India
Dataset contains pollution measurements from various locations.
Pollutants Used
PM2.5
PM10
NO2
OZONE
NH3
SO2
CO
🛠️ Technologies & Libraries Used
Programming Language
Python
Libraries
NumPy
Pandas
Matplotlib
Seaborn
Scikit-learn

Install required libraries using:

pip install numpy pandas matplotlib seaborn scikit-learn
📊 Features of the Project
✅ Data Preprocessing
Handling missing values
Cleaning city/state/station names
Creating pivot tables
Filling null values using mean
✅ AQI Categorization

AQI levels categorized into:

Good
Moderate
Unhealthy for Sensitive
Unhealthy
Hazardous
✅ Data Visualization

The project contains multiple visualizations such as:

Bar Charts
Line Charts
Pie Charts
Histograms
Scatter Plots
Heatmaps
Box Plots
✅ Outlier Detection

Outliers detected using the IQR method and removed for better model performance.

✅ Normalization

Min-Max Normalization applied to pollutant values.

✅ Machine Learning Model

A Linear Regression Model was trained to predict PM2.5 values using:

PM10
NO2
OZONE
NH3
SO2
📈 Machine Learning Workflow
Input Features
['PM10', 'NO2', 'OZONE', 'NH3', 'SO2']
Target Variable
PM2.5
Model Used
Linear Regression
Evaluation Metrics
Mean Squared Error (MSE)
Mean Absolute Error (MAE)
R2 Score
📷 Visualizations Included
AQI Category Distribution
PM2.5 by State
PM10 by State
SO2 Analysis
NH3 Analysis
Correlation Heatmap
Pollutant Scatter Plots
Pollutant Distribution Histograms
Pollution Comparison Across States
Top Polluted Cities
Box Plot Before & After Outlier Removal
Actual vs Predicted PM2.5 Graph

🚀 How to Run the Project
Clone the repository
git clone https://github.com/your-username/your-repository-name.git
Open the project folder
cd your-repository-name
Install required libraries
pip install numpy pandas matplotlib seaborn scikit-learn
Run the Python file
python pythonproject.py

📌 Project Output

The project:

Analyses pollution data from different Indian cities
Identifies highly polluted areas
Detects pollution trends
Predicts PM2.5 levels using machine learning
Visualizes pollution patterns effectively

🔮 Future Improvements
Use advanced ML algorithms like Random Forest or XGBoost
Add real-time AQI API integration
Build an interactive dashboard using Power BI or Streamlit
Deploy the model as a web application
Add time-series forecasting

📚 Learning Outcomes

Through this project, I learned:

Data Cleaning Techniques
Exploratory Data Analysis
Data Visualization
Feature Engineering
Outlier Handling
Machine Learning Model Building
Model Evaluation

👨‍💻 Author

Aditya

⭐ If You Like This Project

Give this repository a ⭐ on GitHub!
