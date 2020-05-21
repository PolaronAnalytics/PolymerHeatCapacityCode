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
import numpy as np
import pandas as pd
from string import split
import string

data_files = open("file_names.txt", "r").readlines()

file_out_1 = open("combine_files.txt", "w")

for j in range(len(data_files)):
    name_spilt = data_files[j].split('.')
    poly_name = name_spilt[1].strip('\n')
    f = open(data_files[j].strip('\n'), "r")
    z = f.readlines()

    file_nos = open(poly_name+"_nos_types.txt", "r").readlines()
    file_types = open(poly_name+"_arr_tot_atomic_types.txt", "r").readlines()

    for i in range(len(file_nos)):
      t_nos = file_nos[i].split()
      t_types = file_types[i].split()
      file_format_1 = "%s %s %s\n"
      if j==0 and i == 0:
         file_out_1.write(file_format_1%tuple(["name", file_nos[i].strip('\n'), file_types[i].strip('\n')]))
      if i > 0:
         file_out_1.write(file_format_1%tuple([poly_name, file_nos[i].strip('\n'), file_types[i].strip('\n')]))
