import numpy as np
import pandas as pd
import sklearn
#from IPython.display import display
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



data = pd.read_csv("../../../csv_files_polymer_data/angle.csv")
data.drop(['name','Cp_KJ/Kg-K', 'Tg'], axis = 1, inplace = True)

#display(data.describe())
#display(data.head(1))


data_copy = data
features = data_copy.drop(["Cp_J/mol-K"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, data["Cp_J/mol-K"], test_size = 0.25, random_state = 42)
#print y_train
###### Calculates and returns the performance score between 
###### true and predicted values based on the metric chosen.
def performance_metric(y_true, y_predict):
   score = r2_score(y_true, y_predict)
   return score

###### Performs grid search over the 'max_depth' parameter for a 
###### decision tree regressor trained on the input data [X, y]. 


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


'''
print "max_depth", "score_train", "score_test"
for k in range(1,30):
  reg_1 = DecisionTreeRegressor(max_depth=k)

  reg_1.fit(X_train, y_train)

  y_1 = reg_1.predict(X_train)
  y_2 = reg_1.predict(X_test)

  print k, performance_metric(y_train,y_1), performance_metric(y_test,y_2)
'''
#file_out_test_1 = open("file_test_1.txt", "w")
#file_out_test_2 = open("file_test_2.txt", "w")

#file_out_train_1 = open("file_train_1.txt", "w")
#file_out_train_2 = open("file_train_2.txt", "w")

#print y_test[1]
#print y_2[0]
'''
file_out_test_1.write("%s"%tuple([y_test]))
for i in range(len(y_2)):
  file_out_test_2.write("%s\n"%tuple([y_2[i]]))


file_out_train_1.write("%s"%tuple([y_train]))
for i in range(len(y_1)):
  file_out_train_2.write("%s\n"%tuple([y_1[i]]))
'''



