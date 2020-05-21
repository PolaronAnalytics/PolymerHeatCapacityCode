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
    file_dihedral_name = open(poly_name+"_tot_dihedral_type_rem_dup.txt", "r").readlines()
    file_out = open(poly_name+"_tot_dihedral_type_rem_dup_again.txt", "w")
#####################################################################
#####################################################################
    name=[]
    num=[]
    cond=[]
    TOT_CT=[]
    sum_ct = 0
### saving the atoms info in arrays######
    for i in range(len(file_dihedral_name)):
      t_tot1 = file_dihedral_name[i].split()
      col_1=t_tot1[0].split('_')
      name.append(str(t_tot1[0]))
      num.append(eval(str(t_tot1[1])))
      cond.append(0)
      TOT_CT.append(0)

    for i in range(len(name)):
     count_1 = num[i]   
     sum_ct = sum_ct+count_1
     for j in range(len(name)):
       if j > i:
        if cond[i]==0 or cond[i]==1:    
         if name[i] == name[j]:
           count_2 = num[j]
           sum_ct = sum_ct+count_2 #tot_count
           TOT_CT[i]=sum_ct
           cond[j]=2
           cond[i]=1
           #  cond[i]=1                 #### this will make sure that it does not repeat on line 17
     sum_ct = 0     
     if cond[i]==0:
        file_out.write("%s %d \n"%tuple([name[i], num[i]]))
     if cond[i]==1:
        file_out.write("%s %d \n"%tuple([name[i], TOT_CT[i]]))

##################################################################
#################################################################

