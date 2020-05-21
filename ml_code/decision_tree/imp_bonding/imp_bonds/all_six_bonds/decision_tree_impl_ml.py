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

data = pd.read_csv("../top_six_bonds.csv")
data.drop(['name','Cp_KJ/Kg-K', 'Tg'], axis = 1, inplace = True)

data_copy = data
features = data_copy.drop(["Cp_J/mol-K"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, data["Cp_J/mol-K"], test_size = 0.25, random_state = 42)
###### Calculates and returns the performance score between 
###### true and predicted values
def performance_metric(y_true, y_predict):
   score = r2_score(y_true, y_predict)
   return score

reg_1 = DecisionTreeRegressor(max_depth=9)
reg_1.fit(X_train, y_train)
y_1 = reg_1.predict(X_train)
y_2 = reg_1.predict(X_test)

print (performance_metric(y_train,y_1), performance_metric(y_test,y_2))

#####################################################################
############### writing train file ###################################
file_out_train = open("file_train_dt.txt", "w")
file_out_train_pred = open("file_train_pred_dt.txt", "w")

file_out_train.write("%s"%tuple([y_train]))

for k in range(len(y_1)):
   file_out_train_pred.write("%f\n"%tuple([y_1[k]]))

#########################################################################
############# writing test file #####################################

file_out_test = open("file_test_dt.txt", "w")
file_out_test_pred = open("file_test_pred_dt.txt", "w")

file_out_test.write("%s"%tuple([y_test]))

for j in range(len(y_2)):
   file_out_test_pred.write("%f\n"%tuple([y_2[j]]))

######################################################################
