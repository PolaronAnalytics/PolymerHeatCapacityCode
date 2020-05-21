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

    file_pairs = open(poly_name+"_pair_ref_name.txt", "r").readlines()
    file_atoms = open(poly_name+"_part_atoms_8.txt", "r").readlines()
    file_out = open(poly_name+"_tot_atomic_types_by_name.txt", "w")

#####################################################################
    count=0
### saving the atoms info in arrays######
    for i in range(len(file_pairs)):
        t_pairs = file_pairs[i].split()
        for j in range(len(file_atoms)):
            t_atoms = file_atoms[j].split()
            if eval(str(t_pairs[1])) == eval(str(t_atoms[2])):
               count=count+1
        file_out.write("%s %d \n"%tuple([t_pairs[0], count]))
        count=0
##################################################################
#################################################################

