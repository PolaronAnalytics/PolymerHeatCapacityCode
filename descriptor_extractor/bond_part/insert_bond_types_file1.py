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

    file_atoms = open(poly_name+"_part_atoms_8.txt", "r").readlines()
    file_bonds = open(poly_name+"_part_bonds_9.txt", "r").readlines()
    file_out = open(poly_name+"_bond_type_11.txt", "w")

    for i in range(len(file_bonds)):
      t_bonds = file_bonds[i].split()
      for j in range(len(file_atoms)):
        t_atoms = file_atoms[j].split()  
        if t_bonds[2] == t_atoms[0]:
          atom_1 = t_atoms[2]
        if t_bonds[3] == t_atoms[0]:
          atom_2 = t_atoms[2]
      file_out.write("%s %s %s %s\n"%tuple([t_bonds[0], t_bonds[1], atom_1, atom_2]))


