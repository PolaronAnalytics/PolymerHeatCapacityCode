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
    file_dihedral_type = open(poly_name+"_dihedral_type_17.txt", "r").readlines()
    file_out = open(poly_name+"_dihedral_pair_coeff_18.txt", "w")

    for i in range(len(file_dihedral_type)):
      t_dihedrals = file_dihedral_type[i].split()
      for j in range(len(file_pairs)):
        t_pairs = file_pairs[j].split()  
        #print t_dihedrals[2], t_atoms[2] 
        if t_dihedrals[2] == t_pairs[0]:
          A_atom1 = t_pairs[1]
          B_atom1 = t_pairs[2]
        if t_dihedrals[3] == t_pairs[0]:
          A_atom2 = t_pairs[1]
          B_atom2 = t_pairs[2]
        if t_dihedrals[4] == t_pairs[0]: 
          A_atom3 = t_pairs[1]
          B_atom3 = t_pairs[2]
        if t_dihedrals[5] == t_pairs[0]:
          A_atom4 = t_pairs[1]
          B_atom4 = t_pairs[2]

      file_out.write("%s %s %s %s %s %s %s %s %s %s\n"%tuple([t_dihedrals[0], t_dihedrals[1], A_atom1, B_atom1, A_atom2, B_atom2, A_atom3, B_atom3, A_atom4, B_atom4]))


