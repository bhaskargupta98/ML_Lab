# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:15:55 2019

@author: student
"""
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing data
dataset = pd.read_csv("stocks.csv")
X = dataset.iloc[:,2:3].values
Y = dataset.iloc[:,4:5].values

#splitting data in training and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 1/3, random_state = 0)


#making linear model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#prediction using predict method of linearregression class

y_pred = regressor.predict(X_test)

#plotting

plt.scatter(X_train, Y_train, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.xlabel("intrest")
plt.ylabel("stock price")
plt.title("linear regression graph")
plt.show()
