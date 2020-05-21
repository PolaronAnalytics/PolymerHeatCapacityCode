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
from string import split
import string

data_files = open("file_names.txt", "r").readlines()

################ this is the 1st file to be used for angle determination ####################

lines_file=[]

for j in range(len(data_files)):
    name_spilt = data_files[j].split('.')
    poly_name = name_spilt[1].strip('\n')
    f = open(data_files[j].strip('\n'), "r")
    z = f.readlines()
    file_angles = open(poly_name+"_tot_angle_type_rem_rep.txt", "r").readlines()
    lines_file.append(len(file_angles))

n = len(data_files)   ### rows
m = max(lines_file)   #### columns
name = [[0] * m for i in range(n)]
num = [[0] * m for i in range(n)]

for j in range(len(data_files)):
    name_spilt = data_files[j].split('.')
    poly_name = name_spilt[1].strip('\n')
    f = open(data_files[j].strip('\n'), "r")
    z = f.readlines()

    file_angles = open(poly_name+"_tot_angle_type_rem_rep.txt", "r").readlines()
    for i in range(len(file_angles)):
      t_angles = file_angles[i].split()
      name[j][i]=t_angles[0]
      num[j][i]=t_angles[1]

u=[]
for j in range(len(data_files)):
  a = name[j][:]
  u = list(set(a+u))

rem=0
for q in range(len(u)):
  if u[q]==0:
     rem=1

if rem==1:
  w = u.remove(0)


cond=[0]*len(u)
for i in range(len(u)):
  name_split_1 = u[i].split('_')
  for j in range(len(u)):  
    if j > i:
      name_split_2 = u[j].split('_')
      if name_split_1[1] == name_split_2[1]:
           if name_split_1[0] == name_split_2[2] and name_split_1[2] == name_split_2[0]:
             cond[i]=1


u1=[0]
for i in range(len(u)):
  if cond[i]==0:
    u1.append(u[i])
#print u
w1 = u1.remove(0)

#print u1

p = len(data_files)   ### rows
q = len(u1)   #### columns
entry = [[0] * q for i in range(p)]

file_out = open("tot_angle_name_combine.txt", "w")
for i in range(len(u1)):
 file_out.write("%s "%tuple([u1[i]]))
file_out.write("\n"%tuple([]))

#############
#### need correction
for i in range(len(u1)):
  name_1 = u1[i].split('_')
  for j in range(len(data_files)):
    for k in range(len(name[j][:])):
      if name[j][k] != 0:
        name_2 = name[j][k].split('_')
        if u1[i]==name[j][k]:
           entry[j][i]=num[j][k]
        if name_1[1] == name_2[1]:
           if name_1[0] == name_2[2] and name_1[2] == name_2[0]:  
              if name_1[0] != name_2[0]:
                 entry[j][i]=num[j][k]
###############################
    
for j in range(len(data_files)):
   for i in range(len(u1)):
     file_out.write("%s "%tuple([entry[j][i]]))
   file_out.write("\n"%tuple([]))




