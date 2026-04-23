import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Objective of My project is :-
#To understand how air pollution levels differ across various cities and states
#To explore the levels of key pollutants like PM2.5, PM10, NO2, and Ozone#
#To observe how pollution values are spread and how much they vary
#To find out if there is any relationship between different pollutants
#To visualize how pollution is distributed geographically using location data
#To identify and rank the most polluted cities or monitoring stations
#To develop a simple model to predict pollution levels based on other factors

#Source:-data.gov.in
#Title is :- Understanding Air Pollution Through Data Analysis and Visualization
#https://www.data.gov.in/resource/real-time-air-quality-index-various-locations



data=pd.read_csv(r"C:\Users\adity\Downloads\aqi.csv")
print(data)
data.columns
print(data[['pollutant_id','pollutant_min','pollutant_max','pollutant_max']])
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', 1000)
data.head()
data.info()
data.describe()
data.isnull().sum()
data['city'] = data['city'].str.strip()
data['state'] = data['state'].str.strip()
data['station'] = data['station'].str.strip()
data['pollutant_avg'].fillna(data['pollutant_avg'].mean(), inplace=True)
data['pollutant_min'].fillna(data['pollutant_min'].mean(), inplace=True)
data['pollutant_max'].fillna(data['pollutant_max'].mean(), inplace=True)
data.isnull().sum()
pivotData = data.pivot_table(index=['state', 'city', 'last_update'],columns='pollutant_id',values='pollutant_avg').reset_index()
pivotData
pivotData.columns
print(pivotData[['state','OZONE','CO','NH3','SO2','PM2.5','PM10','NO2']])
pivotData.head(200)
pivotData.isnull().sum()
for col in ['PM2.5','PM10','NO2','OZONE','NH3','SO2','CO']:
    pivotData[col].fillna(pivotData[col].mean(), inplace=True)
pivotData.isnull().sum()
#AQI CATEGORIZE
def categorize(pm):
    if pm <= 50:
        return 'Good'
    elif pm <= 100:
        return 'Moderate'
    elif pm <= 150:
        return 'Unhealthy for Sensitive'
    elif pm <= 200:
        return 'Unhealthy'
    else:
        return 'Hazardous'

pivotData['AQI_Category'] = pivotData['PM2.5'].apply(categorize)

#This Bar Chart Show that How Category of pollutants distributed in numbers
plt.figure(figsize=(12,8))
city_counts = pivotData.groupby('AQI_Category')['city'].nunique()
plt.bar(city_counts.index, city_counts.values,color='blue',edgecolor='r')
plt.title('Number of Cities in Each AQI Category',fontsize=30)
plt.xlabel('AQI Category')
plt.ylabel('Number of Cities')
plt.show()

# Average PM2.5 per state
#This Bar Plot present the avg of PM2.5 pollutant in different state
plt.figure(figsize=(20,8))
state_pollution = pivotData.groupby('state')['PM2.5'].mean()
plt.bar(state_pollution.index, state_pollution.values,edgecolor='black')
plt.title('PM2.5 by State',fontsize=30,color='blue')
plt.xlabel('State',fontsize=20)
plt.ylabel('PM2.5',fontsize=20)
plt.xticks(rotation=90,fontsize=25)
plt.yticks(rotation=0,fontsize=25)
plt.show()

#This Bar Plot present the avg of PM10 pollutant in different state
plt.figure(figsize=(30,18))
state_pollution = pivotData.groupby('state')['PM10'].mean()
plt.bar(state_pollution.index, state_pollution.values,color='red', edgecolor='black', width=0.9)
plt.title('PM10 by State',fontsize=40,color='r')
plt.xlabel('State',fontsize=40,color='r')
plt.ylabel('PM10',fontsize=40,color='r')
plt.xticks(rotation=90,fontsize=35)
plt.yticks(rotation=0,fontsize=35)
plt.tight_layout()
plt.show()

#This Bar Plot present the avg of NO2 pollutant in different state
plt.figure(figsize=(30,10))
state_pollution = pivotData.groupby('state')['NO2'].mean()
plt.bar(state_pollution.index, state_pollution.values,color='red',edgecolor='black')
plt.title('NO2 by State',fontsize=60)
plt.xlabel('State',fontsize=35)
plt.ylabel('NO2',fontsize=35)
plt.xticks(rotation=90,fontsize=30)
plt.yticks(rotation=0,fontsize=30)
plt.show()

#This Bar Plot present the avg of OZONE pollutant in different state
plt.figure(figsize=(30,10))
state_pollution = pivotData.groupby('state')['OZONE'].mean()
plt.bar(state_pollution.index, state_pollution.values,color='green',edgecolor='black')
plt.title('OZONE by State',fontsize=60)
plt.xlabel('State',fontsize=35)
plt.ylabel('OZONE',fontsize=35)
plt.xticks(rotation=90,fontsize=30)
plt.yticks(rotation=0,fontsize=30)
plt.show()

#This Bar Plot present the avg of S02  pollutant in different state
plt.figure(figsize=(30,10))
state_pollution = pivotData.groupby('state')['SO2'].mean()
plt.bar(state_pollution.index, state_pollution.values,color='brown')
plt.title('SO2 by State',fontsize=60)
plt.xlabel('State',fontsize=35)
plt.ylabel('SO2',fontsize=35)
plt.xticks(rotation=90,fontsize=30)
plt.yticks(rotation=0,fontsize=30)
plt.show()

#This Bar Plot present the avg of NH3  pollutant in different state
plt.figure(figsize=(30,10))
state_pollution = pivotData.groupby('state')['NH3'].mean()
plt.bar(state_pollution.index, state_pollution.values,color='green')
plt.title('NH3 by State',fontsize=60)
plt.xlabel('State',fontsize=35)
plt.ylabel('NH3',fontsize=35)
plt.xticks(rotation=90,fontsize=30)
plt.yticks(rotation=0,fontsize=30)
plt.show()


#This Bar Plot present the avg of carbonMonoxide(CO)  pollutant in different state
plt.figure(figsize=(20,8))
state_pollution = pivotData.groupby('state')['CO'].mean()
plt.bar(state_pollution.index, state_pollution.values,color='green')
plt.title('Carbon Monoxide by State',fontsize=60)
plt.xlabel('State',fontsize=30)
plt.ylabel('Carbon Monoxide',fontsize=30)
plt.xticks(rotation=90,fontsize=30)
plt.yticks(rotation=0,fontsize=30)
plt.show()



#This visuals represnts the correlation between all pollutants
pollutants = pivotData[['PM2.5', 'PM10', 'NO2', 'OZONE','SO2','CO','NH3']]
corr = pollutants.corr() #Finding correlation
corr
#The heatmap shows the correlation between different pollutants.
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True)
plt.title('Correlation Between Pollutants')
plt.show()
# Strong positive correlations indicate that certain pollutants tend to increase together, 
#which may be due to similar sources or environmental conditions.

plt.scatter(pivotData['PM10'], pivotData['PM2.5'], alpha=0.7,color='blue')
plt.xlabel('PM10')
plt.ylabel('PM2.5')
plt.title('PM2.5 vs PM10')
plt.show()


plt.scatter(pivotData['NO2'], pivotData['PM2.5'], alpha=0.5)
plt.xlabel('NO2')
plt.ylabel('PM2.5')
plt.title('PM2.5 vs NO2')
plt.show()

plt.scatter(pivotData['OZONE'], pivotData['PM2.5'], alpha=0.5)
plt.xlabel('OZONE')
plt.ylabel('PM2.5')
plt.title('PM2.5 vs OZONE')
plt.show()


plt.scatter(pivotData['NH3'], pivotData['PM2.5'], alpha=0.5)
plt.xlabel('NH3')
plt.ylabel('PM2.5')
plt.title('PM2.5 vs NH3')
plt.show()


plt.scatter(pivotData['SO2'], pivotData['PM2.5'], alpha=0.5)
plt.xlabel('SO2')
plt.ylabel('PM2.5')
plt.title('PM2.5 vs SO2')
plt.show()


plt.scatter(pivotData['NH3'], pivotData['SO2'], alpha=0.5)
plt.xlabel('NH3')
plt.ylabel('SO2')
plt.title('NH3 vs SO2')
plt.show()

plt.scatter(pivotData['CO'], pivotData['PM2.5'], alpha=0.5)
plt.xlabel('CO')
plt.ylabel('PM2.5')
plt.title('PM2.5 vs CO')
plt.show()


plt.scatter(pivotData['CO'], pivotData['NO2'], alpha=0.5)
plt.xlabel('CO')
plt.ylabel('NO2')
plt.title('CO vs NO2')
plt.show()


plt.scatter(pivotData['CO'], pivotData['PM10'], alpha=0.5)
plt.xlabel('CO')
plt.ylabel('PM10')
plt.title('CO vs PM10')
plt.show()

#Hisplots to show distribution of all pollutants 
plt.hist(pivotData['PM2.5'], bins=10,color='brown',edgecolor='black')
plt.title('PM2.5 Distribution')
plt.show()

plt.hist(pivotData['PM10'], bins=10)
plt.title('PM10 Distribution')
plt.show()

plt.hist(pivotData['NO2'], bins=10)
plt.title('NO2 Distribution')
plt.show()

plt.hist(pivotData['OZONE'], bins=10)
plt.title('OZONE Distribution')
plt.show()

plt.hist(pivotData['NH3'], bins=10)
plt.title('NH3 Distribution')
plt.show()

plt.hist(pivotData['SO2'], bins=10)
plt.title('SO2 Distribution')
plt.show()

plt.hist(pivotData['CO'], bins=10)
plt.title('CO Distribution')
plt.show()




pollutant_mean = pivotData[['PM2.5','PM10','NO2','OZONE','NH3','SO2','CO']].mean()
plt.figure(figsize=(7,7))
plt.pie(pollutant_mean, labels=pollutant_mean.index, autopct='%1.1f%%')
plt.title('Pollutants distibution in Total pollution',fontsize=40,color='red')
plt.show()


#This chart will show top 10 states with lowest pollutants distribution
top_states = pivotData.groupby('state')[['PM2.5','PM10','NO2','OZONE','SO2','NH3','CO']].mean()
top_states = top_states.sort_values(by='PM2.5', ascending=False).head(10)
plt.figure(figsize=(16,8))
plt.plot(top_states.index, top_states['PM2.5'], marker='o', label='PM2.5')
plt.plot(top_states.index, top_states['PM10'], marker='o', label='PM10')
plt.plot(top_states.index, top_states['NO2'], marker='o', label='NO2')
plt.plot(top_states.index, top_states['OZONE'], marker='o', label='OZONE')
plt.plot(top_states.index, top_states['SO2'], marker='o', label='SO2')
plt.plot(top_states.index, top_states['NH3'], marker='o', label='NH3')
plt.plot(top_states.index, top_states['CO'], marker='o', label='CO')
plt.title('Pollution Comparison (Top States)',fontsize=40)
plt.xlabel('State',fontsize=25)
plt.ylabel('Pollution Level',fontsize=25)
plt.xticks(rotation=90,fontsize=20)
plt.yticks(rotation=0,fontsize=20)
plt.legend()
plt.show()


#This chart will show top 10 states with lowest pollutants distribution
low_states = pivotData.groupby('state')[['PM2.5','PM10','NO2','OZONE','SO2','NH3','CO']].mean()
low_states = low_states.sort_values(by='PM2.5', ascending=True).head(10)
plt.figure(figsize=(14,8))
for col in ['PM2.5','PM10','NO2','OZONE','SO2','NH3','CO']:
    plt.plot(low_states.index, low_states[col], marker='o', label=col)
plt.title('Top less polluted cities', fontsize=25)
plt.xlabel('State', fontsize=25)
plt.ylabel('Pollution Level', fontsize=25)
plt.xticks(rotation=90, fontsize=20)
plt.yticks(fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

#This visuals Shows that top 10 cities where pollutants are highly contributed
top_cities = pivotData.groupby('city')[['PM2.5','PM10','NO2','NH3','SO2','CO','OZONE']].mean()
top_cities = top_cities.sort_values(by='PM2.5', ascending=False).head(10)
plt.figure(figsize=(14,8))
for col in ['PM2.5','PM10','NO2','CO','NH3','SO2','OZONE']:
    plt.plot(top_cities.index, top_cities[col], marker='o', label=col)
plt.title('Top Cities Pollution Comparison', fontsize=25)
plt.xlabel('City', fontsize=24)
plt.ylabel('Pollution Level', fontsize=24)
plt.xticks(rotation=90, fontsize=20)
plt.yticks(fontsize=20)
plt.legend()
plt.tight_layout()
plt.show()

#This visuals Shows that top 10 cities where pollutants are less contributed
low_cities = pivotData.groupby('city')[['PM2.5','PM10','NO2','NH3','SO2','CO','OZONE']].mean()
low_cities = low_cities.sort_values(by='PM2.5', ascending=True).head(10)
plt.figure(figsize=(14,8))
for col in ['PM2.5','PM10','NO2','CO','NH3','SO2','OZONE']:
    plt.plot(low_cities.index, low_cities[col], marker='o', label=col)
plt.title('Top less polluted Cities', fontsize=25)
plt.xlabel('City', fontsize=24)
plt.ylabel('Pollution Level', fontsize=24)
plt.xticks(rotation=90, fontsize=20)
plt.yticks(fontsize=20)
plt.legend()
plt.tight_layout()
plt.show()

#This Box plot also helps to detect outliers
pivotData[['PM2.5','PM10','NO2','OZONE','CO','SO2','NH3']].boxplot()
plt.title('Pollutant Distribution (Box Plot)')
plt.ylabel('Values')
plt.show()
#Outliers detected in visuals
outliers = []
numeric_cols = ['PM2.5','PM10','NO2','OZONE','CO','SO2','NH3']
for col in numeric_cols:
    Q1 = pivotData[col].quantile(0.25)
    Q3 = pivotData[col].quantile(0.75)
    IQR = Q3 - Q1   
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers.extend(pivotData[(pivotData[col] < lower_bound) | (pivotData[col] > upper_bound)].index)
outliers = list(set(outliers))
outliers
clean_data = pivotData.drop(outliers)
print("Outliers removed successfully")
clean_data[['PM2.5','PM10','NO2','OZONE','CO','SO2','NH3']].boxplot()
plt.title('Box Plot of Pollutants After Removing All Outliers')
plt.ylabel('Values')
plt.show()



#This is the list of dangerous cities in india before and after removing outliers
# Before cleaning
DangCities_before = pivotData[pivotData['AQI_Category'] == 'Unhealthy for Sensitive']['city'].unique()
# After cleaning
DangCities_after = clean_data[clean_data['AQI_Category'] == 'Unhealthy for Sensitive']['city'].unique()
print("Before Cleaning:", DangCities_before)
print("After Cleaning:", DangCities_after)



# NORMALIZATION (MIN-MAX)
cols = ['PM2.5','PM10','NO2','OZONE','NH3','SO2']
for col in cols:    
    min_val = clean_data[col].min()
    max_val = clean_data[col].max()    
    clean_data[col] = (clean_data[col] - min_val) / (max_val - min_val)
print("Normalization is done")
print(clean_data[cols].describe())


danger_cities = clean_data.groupby('city')['PM2.5'].mean().sort_values(ascending=False).head(10)
print("Top 10 Most Polluted Cities:")
print(danger_cities)

clean_cities = clean_data.groupby('city')['PM2.5'].mean().sort_values(ascending=True).head(10)
print("Top 10 Least Polluted Cities:")
print(clean_cities)

category_count = clean_data['AQI_Category'].value_counts()
print("AQI Category Distribution:")
print(category_count)

ufs_cities = clean_data[clean_data['AQI_Category'] == 'Unhealthy for Sensitive']['city'].unique()
print("Cities with Unhealthy for Sensitive AQI:")
for city in ufs_cities:
    print(city)    
corr = clean_data[['PM2.5','PM10','NO2','OZONE','NH3','SO2']].corr()
print("Correlation Matrix:")
print(corr)
print("Analysis Completed Successfully")


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


df = clean_data.copy()
X = df[['PM10','NO2','OZONE','NH3','SO2']]   # Input
Y = df[['PM2.5']]                            # Output
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)
model = LinearRegression()
model.fit(X_train, Y_train)
PM10_val = 100
NO2_val = 40
OZONE_val = 30
NH3_val = 20
SO2_val = 10
sample_input = pd.DataFrame({
    'PM10':[PM10_val],
    'NO2':[NO2_val],
    'OZONE':[OZONE_val],
    'NH3':[NH3_val],
    'SO2':[SO2_val]
})
prediction = model.predict(sample_input)
# extract value
pred_value = prediction[0][0]
# get category
category = categorize(pred_value)
# print both
print(f"Predicted PM2.5: {pred_value:.2f}")
print("AQI Category:", category)
#Use REAL DATA as input
real_sample = X_test.iloc[[0]]
print("\nInput from Data:\n", real_sample)
real_prediction = model.predict(real_sample)
print(f"Predicted PM2.5 (real data): {real_prediction[0][0]:.4f}")
#Scatter Plot (Actual vs Predicted)
Y_pred = model.predict(X_test)
plt.scatter(Y_test, Y_pred,color='r')
sns.regplot(x=Y_test, y=Y_pred)
plt.xlabel("Actual PM2.5")
plt.ylabel("Predicted PM2.5")
plt.title("Actual vs Predicted PM2.5")
plt.grid(True)
plt.show()

#The regression plot shows that as actual PM2.5 values increase, 
#the predicted values also increase, so the model is able to capture the general trend.
#However, the points are quite scattered around the line, which means 
#the predictions are not very accurate. The model especially struggles with higher pollution values, 
#where the errors become more noticeable.
#Overall, it gives a rough idea of PM2.5 levels but isn’t very precise.

#Model Evaluation
#Mean Square Error
mse = mean_squared_error(Y_test, Y_pred)
print(f"\nMean Squared Error: {mse:.2f}")
#R2-Score
r2 = r2_score(Y_test, Y_pred)
print(f"R2 Score: {r2:.2f}")
result = pd.DataFrame({'Actual': Y_test.values.flatten(),'Predicted': Y_pred.flatten()})
print(result.head(10))
result['Error'] = result['Actual'] - result['Predicted']
print(result.head())
#Mean Absolute error
mae = mean_absolute_error(Y_test, Y_pred)
print(f"\nMean Absolute Error: {mae:.2f}")
corr = df[['PM2.5','PM10','NO2','OZONE','NH3','SO2','CO']].corr()
print(corr['PM2.5'])
######################################################################