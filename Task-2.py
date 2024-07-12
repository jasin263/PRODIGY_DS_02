import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the matplotlib backend to Agg
import matplotlib
matplotlib.use('Agg')

# Load the dataset
titanic_data = pd.read_csv('E:\\INRERN PROJECTS\\TASK-2\\Titanicdataset.csv')

# Display the first few rows
print(titanic_data.head())

# Check for missing values
missing_values = titanic_data.isnull().sum()
print(missing_values)

# Drop the Cabin column
titanic_data_cleaned = titanic_data.drop(columns=['Cabin'])

# Fill missing values in Age with the median age
median_age = titanic_data_cleaned['Age'].median()
titanic_data_cleaned.loc[:, 'Age'] = titanic_data_cleaned['Age'].fillna(median_age)

# Fill missing value in Fare with the median fare
median_fare = titanic_data_cleaned['Fare'].median()
titanic_data_cleaned.loc[:, 'Fare'] = titanic_data_cleaned['Fare'].fillna(median_fare)

# Verify that there are no missing values left
missing_values_cleaned = titanic_data_cleaned.isnull().sum()
print(missing_values_cleaned)

# Distribution of passengers by class
plt.figure(figsize=(8, 6))
sns.countplot(data=titanic_data_cleaned, x='Pclass')
plt.title('Distribution of Passengers by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.savefig('passengers_by_class.png')
plt.close()

# Distribution of passengers by gender
plt.figure(figsize=(8, 6))
sns.countplot(data=titanic_data_cleaned, x='Sex')
plt.title('Distribution of Passengers by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.savefig('passengers_by_gender.png')
plt.close()

# Distribution of passengers by age
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic_data_cleaned, x='Age', bins=30, kde=True)
plt.title('Distribution of Passengers by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('passengers_by_age.png')
plt.close()

# Distribution of passengers by embarkation point
plt.figure(figsize=(8, 6))
sns.countplot(data=titanic_data_cleaned, x='Embarked')
plt.title('Distribution of Passengers by Embarkation Point')
plt.xlabel('Embarkation Point')
plt.ylabel('Count')
plt.savefig('passengers_by_embarkation.png')
plt.close()

# Distribution of fare prices
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic_data_cleaned, x='Fare', bins=30, kde=True)
plt.title('Distribution of Fare Prices')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.savefig('fare_prices.png')
plt.close()

print("NOTE: The output of distributions is saved")
