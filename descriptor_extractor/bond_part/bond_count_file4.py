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

    file_bond_name = open(poly_name+"_bond_name_13.txt", "r").readlines()
    file_out = open(poly_name+"_tot_bond_type.txt", "w")

#####################################################################
### saving the atoms info in arrays######
    count=1
    for i in range(len(file_bond_name)):
        t_tot1 = file_bond_name[i].split()
        for j in range(len(file_bond_name)):
            t_tot2 = file_bond_name[j].split()
            if j > i:
              if eval(str(t_tot1[1])) == eval(str(t_tot2[1])):
                count=count+1
        file_out.write("%s %s %d \n"%tuple([t_tot1[2]+"_"+t_tot1[3], t_tot1[1], count]))
        count=1
##################################################################
#################################################################

