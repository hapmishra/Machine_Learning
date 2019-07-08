#in this program i am going to import the inbuilt dataset in sklearn library
#called Iris dataset and going to find its insights

#importing the required libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
from sklearn.datasets import load_iris
 
#loading the iris dataset in variable named "dataset"
dataset=load_iris()

#now assigning the feature matrics to variable named "feature_matrics" and target
#named "target"
feature_matrics = dataset.data 
target = dataset.target

#now i am comparing the patel length and patel width

mp.scatter(feature_matrics[target==0,2],feature_matrics[target==0,3],c='g',label="satosa")
mp.scatter(feature_matrics[target==1,2],feature_matrics[target==1,3],c="b",label="versicolor")
mp.scatter(feature_matrics[target==2,2],feature_matrics[target==2,3],c="r",label="virginica")
mp.xlabel("Patel Length")
mp.ylabel("Patel Width")
mp.legend()
mp.show()
