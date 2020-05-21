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

################ this is the 1st file to be used for bond determination ####################
for j in range(len(data_files)):
    name_spilt = data_files[j].split('.')
    poly_name = name_spilt[1].strip('\n')
    f = open(data_files[j].strip('\n'), "r")
    z = f.readlines()

    file_pairs = open(poly_name+"_part_pairs_4.txt", "r").readlines()
    file_bond_type = open(poly_name+"_bond_type_11.txt", "r").readlines()
    file_out = open(poly_name+"_bond_pair_coeff_12.txt", "w")

    for i in range(len(file_bond_type)):
      t_bonds = file_bond_type[i].split()
      for j in range(len(file_pairs)):
        t_pairs = file_pairs[j].split()  
        #print t_angles[2], t_atoms[2] 
        if t_bonds[2] == t_pairs[0]:
          A_atom1 = t_pairs[1]
          B_atom1 = t_pairs[2]
        if t_bonds[3] == t_pairs[0]:
          A_atom2 = t_pairs[1]
          B_atom2 = t_pairs[2]
      file_out.write("%s %s %s %s %s %s\n"%tuple([t_bonds[0], t_bonds[1], A_atom1, B_atom1, A_atom2, B_atom2]))


