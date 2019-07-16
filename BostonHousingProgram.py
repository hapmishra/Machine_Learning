#importing libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as mp

#loading dataset from sklearn library
from sklearn.datasets import load_boston
boston_data=load_boston()

#creating feature matric from given dataset
feature_matric=pd.DataFrame(boston_data.data)

feature_matric.columns=boston_data.feature_names#setting columns names
#according to the description

#setting vector of prediction and the name of the column
vector_of_prediction=pd.DataFrame(boston_data.target)
vector_of_prediction.columns=["Price"]

#training model from given dataset
from sklearn.model_selection import train_test_split
feature_matric_train,feature_matric_test,vector_of_prediction_train,vector_of_prediction_test=train_test_split(feature_matric,vector_of_prediction,test_size=0.60,random_state=5)



from sklearn.linear_model import LinearRegression
LinearRegression=LinearRegression()
LinearRegression.fit(feature_matric_train,vector_of_prediction_train)

LinearRegression.predict(feature_matric_test)
