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

    file_angle_name = open(poly_name+"_angle_name_16.txt", "r").readlines()
    file_out = open(poly_name+"_tot_angle_type.txt", "w")

#####################################################################
    type_ref=[]
    count=1
    tag=0
### saving the atoms info in arrays######
    for i in range(len(file_angle_name)):
        t_tot1 = file_angle_name[i].split()
        for j in range(len(file_angle_name)):
            t_tot2 = file_angle_name[j].split()
            if j > i:
              if eval(str(t_tot1[1])) == eval(str(t_tot2[1])):
                count=count+1
        file_out.write("%s %s %d \n"%tuple([t_tot1[2]+"_"+t_tot1[3]+"_"+t_tot1[4], t_tot1[1], count]))
        count=1
##################################################################
#################################################################

