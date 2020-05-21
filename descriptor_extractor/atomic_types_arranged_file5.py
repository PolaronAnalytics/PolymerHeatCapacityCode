'''
#################################################################################################
The software is developed by Rahul Bhowmik of Polaron Analytics 
For any questions contact via email: rahulbhowmik@polaronanalytics.com or bhowmikrahul@gmail.com
#################################################################################################
This software is distributed under the GNU General Public License.
#################################################################################################
'''

import sys
import os
import math
from sys import argv, exit
import numpy
from string import split
import string

data_files = open("file_names.txt", "r").readlines()

for j in range(len(data_files)):
    name_spilt = data_files[j].split('.')
    poly_name = name_spilt[1].strip('\n')
    f = open(data_files[j].strip('\n'), "r")
    z = f.readlines()
   
    file_types = open(poly_name+"_tot_atomic_types_by_name.txt", "r").readlines()
    file_out = open(poly_name+"_arr_tot_atomic_types.txt", "w")

    name=[]
    nos=[]
#####################################
### saving the pait coeffs in arrays######
    for i in range(len(file_types)):
      t_types = file_types[i].split()
      name.append(t_types[0])
      nos.append(t_types[1])
##################################################################
    for i in range(len(name)):
      file_out.write("%s "%tuple([name[i]]))
    file_out.write("\n"%tuple([]))

    for i in range(len(name)):
      file_out.write("%s "%tuple([nos[i]]))



