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

    file_dihedral_name = open(poly_name+"_tot_dihedral_type_rem_dup_again.txt", "r").readlines()
    file_out = open(poly_name+"_tot_dihedral_type_rem_rep.txt", "w")

#####################################################################
#####################################################################
    name=[]
    num=[]
    name_part1=[]
    name_part2=[]
    name_part3=[]
    name_part4=[]
    cond=[]
    TOT_CT=[]
    sum_ct = 0
### saving the atoms info in arrays######
    for i in range(len(file_dihedral_name)):
      t_tot1 = file_dihedral_name[i].split()
      col_1=t_tot1[0].split('_')
      name.append(t_tot1[0])
      num.append(eval(str(t_tot1[1])))
      name_part1.append(col_1[0])
      name_part2.append(col_1[1])
      name_part3.append(col_1[2])
      name_part4.append(col_1[3])
      cond.append(0)
      TOT_CT.append(0)

    for i in range(len(name)):
     for j in range(len(name)):
       if j > i:
        if cond[i]==0:
         if name_part2[i] == name_part3[j] and name_part2[j] == name_part3[i]:
           if name_part1[i] == name_part4[j] and name_part1[j] == name_part4[i]:
             count_1 = num[i]
             count_2 = num[j]
             tot_count = count_1+count_2
             sum_ct = sum_ct+tot_count
             TOT_CT[i]=sum_ct
             cond[j]=2
             cond[i]=1                 #### this will make sure that it does not repeat on line 17
     sum_ct = 0
    for i in range(len(name)):
       if cond[i]==0:
         file_out.write("%s %d \n"%tuple([name[i], num[i]]))
       if cond[i]==1:
         file_out.write("%s %d \n"%tuple([name[i], TOT_CT[i]]))

##################################################################
#################################################################

