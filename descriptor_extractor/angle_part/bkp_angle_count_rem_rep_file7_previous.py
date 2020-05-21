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

    file_angle_name = open(poly_name+"_tot_angle_type_rem_dup_again.txt", "r").readlines()
    file_out = open(poly_name+"_tot_angle_type_rem_rep.txt", "w")

#####################################################################
#####################################################################
    name=[]
    num=[]
    name_part1=[]
    name_part2=[]
    name_part3=[]
    cond=[]

### saving the atoms info in arrays######
    for i in range(len(file_angle_name)):
      t_tot1 = file_angle_name[i].split()
      col_1=t_tot1[0].split('_')
      name.append(t_tot1[0])
      num.append(eval(str(t_tot1[1])))
      name_part1.append(col_1[0])
      name_part2.append(col_1[1])
      name_part3.append(col_1[2])
      cond.append(0)

    for i in range(len(name)):
     for j in range(len(name)):
       if j > i:
         if name_part2[i] == name_part2[j]:
           if name_part1[i] == name_part3[j] and name_part1[j] == name_part3[i]:
             count_1 = num[i]
             count_2 = num[j]
             tot_count = count_1+count_2
             cond[j]=1
             cond[i]=2                 #### this will make sure that it does not repeat on line 17
     if cond[i]==0:
       file_out.write("%s %d \n"%tuple([name[i], num[i]]))
     if cond[i]==1:
       file_out.write("%s %d \n"%tuple([name[i], tot_count]))

##################################################################
#################################################################

