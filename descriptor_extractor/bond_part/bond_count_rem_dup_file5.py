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

    file_bond_name = open(poly_name+"_tot_bond_type.txt", "r").readlines()
    file_out = open(poly_name+"_tot_bond_type_rem_dup.txt", "w")

#####################################################################
    col_1_name=[]
    col_2_type=[]
    col_3_count=[]
### saving the atoms info in arrays######
    for i in range(len(file_bond_name)):
        t_tot1 = file_bond_name[i].split()
        col_2_type.append(t_tot1[1])

    def removeDuplicates(listofElements):
    # Create an empty list to store unique elements
        uniqueList = []
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
        for elem in listofElements:
           if elem not in uniqueList:
              uniqueList.append(elem)
    # Return the list of unique elements        
        return uniqueList
 
    # Remove duplicates from list by keeping the order as original
    listOfNums = removeDuplicates(col_2_type)

    for k in range(len(listOfNums)):
      for i in range(len(file_bond_name)):
        t_tot1 = file_bond_name[i].split()
        if eval(str(listOfNums[k])) == eval(str(t_tot1[1])):
           file_out.write("%s %s\n"%tuple([t_tot1[0], t_tot1[2]]))
           break


#################################################################

