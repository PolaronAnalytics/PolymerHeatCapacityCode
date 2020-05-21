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

    file_pairs = open(poly_name+"_part_pairs_4.txt", "r").readlines()
    file_reference = open("mass_pair_coeff.txt", "r").readlines()
    file_out = open(poly_name+"_pair_ref_name.txt", "w")

#####################################################################
    LJ_A=[]
    LJ_B=[]
    No=[]
####################################################################
### saving the pair coeffs in arrays######
    for i in range(len(file_pairs)):
        t_pairs = file_pairs[i].split()
        LJ_A.append(eval(str(t_pairs[1])))
        LJ_B.append(eval(str(t_pairs[2])))
        No.append(eval(str(t_pairs[0])))
##################################################################
###########checking the atom name from reference file############# 
    name=[]
    count=0
    num=0
    for i in range(len(file_reference)):
        t_ref = file_reference[i].split()
        #file_format_1 = "%s"
        if file_reference[i] != '\n':
         if t_ref[0] != "###":
           if t_ref[0] != "No":
             count=0  ### "count" is used to make sure that output has those names which do not have pait coef in the current data file
             for j in range(len(file_pairs)):         
               if LJ_A[j]-0.0001< eval(str(t_ref[3]))<LJ_A[j]+0.0001 and LJ_B[j]-0.0001< eval(str(t_ref[4]))<LJ_B[j]+0.0001:
               #if eval(str(t_ref[3])) == LJ_A[j] and eval(str(t_ref[4])) == LJ_B[j]:
                  file_out.write("%s %d \n"%tuple([t_ref[2], No[j]]))
                  count=1
                  num=num+1
             if count==0:
                file_out.write("%s %d \n"%tuple([t_ref[2], 0])) #### if the ref name is not present the it will output "0"
################################################################
#### the below lines will check the reference file has all the types present in the data file ###########
    if num != len(file_pairs):
      print poly_name, "Warning: check the refernce file and the data pair nos"

