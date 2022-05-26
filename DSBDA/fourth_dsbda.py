# -*- coding: utf-8 -*-
"""Fourth_DSBDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19yiPgVC8IuVxSurl1OZp-mAc-9d8oPba
"""

# Commented out IPython magic to ensure Python compatibility.
# loading all libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
# When using the 'inline' backend, your matplotlib graphs will be included in your notebook, next to the code. 
# %matplotlib inline

# load the housing data from the scikit-learn library
from sklearn.datasets import load_boston

boston_dataset = load_boston()

# We print the value of the boston_dataset to understand what it contains.
print(boston_dataset.keys())

# load dataset into pandas DataFrame and print dataset (first 5 values)
df = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
df.head()

# as price column is missing need to create column of target values in dataframe
df['Price'] = boston_dataset.target
df.head()

# describe the boston dataset
df.describe()

# info of boston dataset
df.info()

# checking the missing values using isnull()
df.isnull().sum()

# setting the output figure size
sns.set(rc={'figure.figsize':(11.7, 8.27)})
# plotting the target value Price for visualsing through histogram
sns.displot(df['Price'], bins=30)
plt.show()

# correlation matrix to measure the linear relationships between the variables.
correlation_matrix = df.corr().round(2)
# annot - true to print value inside square
# use the heatmap function from the seaborn library to plot the matrix
sns.heatmap(data=correlation_matrix, annot=True)

# By observing correlation matrix we can see that RM has a strong positive correlation
# with Price (0.7) and LSTAT has a high negative correlation with Price (-0.74)
# RM and LSTAT are used as features
plt.figure(figsize=(20, 5))
features = ['LSTAT', 'RM']
target = df['Price']

for i, col in enumerate(features):
  plt.subplot(1, len(features), i+1)
  x = df[col]
  y = target
  plt.scatter(x, y, marker='o')
  plt.title(col)
  plt.xlabel(col)
  plt.ylabel('MEDV')

# We concatenate the LSTAT and RM columns using np.c_ provided by the numpy library
import numpy as np
X = pd.DataFrame(np.c_[df['LSTAT'], df['RM']], columns=['LSTAT','RM'])
Y = df['Price']

# We train the model with 80% of the samples and test with the remaining 20%
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=5)
# print the sizes of our training and test set to verify if the splitting is proper
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)

# model evaluation
from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X_test)
# root mean squared error
rmse = (np.sqrt(mean_squared_error(Y_test, y_pred)))
r2 = r2_score(Y_test, y_pred)
print('the model performance for testing set')
print('-------------------------------------')
print(f'RMSE is {rmse}')
print(f'R2 score is {r2}')

# produce matrix for sample data
sample_data = [[6.89, 9.939]]
price = model.predict(sample_data)
print(f"predicted selling price for house : {price[0]:.2f}")

