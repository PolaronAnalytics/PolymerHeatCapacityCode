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

    file_rep = open(poly_name+"_tot_dihedral_type_rem_rep.txt", "r").readlines()

#####################################################################
    count=0
### saving the atoms info in arrays######
    for i in range(len(file_rep)):
        t_pairs = file_rep[i].split()
        count=count+eval(str(t_pairs[1]))

    file_tot_dihed = open("tot_dihedral_name_combine.txt", "r").readlines()

    sum_ct = 0
    no_split = file_tot_dihed[j+1].split()
    for n in range(len(no_split)):
        sum_ct = sum_ct + eval(str(no_split[n]))
        #print sum_ct
    print count, sum_ct
##################################################################
#################################################################

