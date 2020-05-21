'''
#################################################################################################
The software is developed by Rahul Bhowmik of Polaron Analytics 
For any questions contact via email: rahulbhowmik@polaronanalytics.com or bhowmikrahul@gmail.com
#################################################################################################
This software is distributed under the GNU General Public License.
#################################################################################################
'''

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import make_scorer
import matplotlib.pyplot as plt
import os
from subprocess import call

from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPRegressor

data = pd.read_csv("../../csv_files_polymer_data/combine_all_29Oct19.csv")
data.drop(['name','Cp_KJ/Kg-K', 'Tg'], axis = 1, inplace = True)

data_copy = data
features = data_copy.drop(["Cp_J/mol-K"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, data["Cp_J/mol-K"], test_size = 0.25, random_state = 42)
###### Calculates and returns the performance score between 
###### true and predicted values based on the metric chosen.
def performance_metric(y_true, y_predict):
   score = r2_score(y_true, y_predict)
   return score

###### Performs grid search over the 'max_depth' parameter for a 
###### decision tree regressor trained on the input data [X, y]. 


print ("max_depth", "score_train", "score_test")
for k in range(1,31):
  reg_1 = DecisionTreeRegressor(max_depth=k)

  reg_1.fit(X_train, y_train)

  y_1 = reg_1.predict(X_train)
  y_2 = reg_1.predict(X_test)

  print (k, performance_metric(y_train,y_1), performance_metric(y_test,y_2))




