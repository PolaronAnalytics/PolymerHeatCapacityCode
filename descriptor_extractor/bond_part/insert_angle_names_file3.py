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

    file_pairs = open("mass_pair_coeff.txt", "r").readlines()
    file_bond_pair = open(poly_name+"_bond_pair_coeff_12.txt", "r").readlines()
    file_out = open(poly_name+"_bond_name_13.txt", "w")

    for i in range(len(file_bond_pair)):
      t_bonds = file_bond_pair[i].split()
      for j in range(len(file_pairs)):
        t_pairs = file_pairs[j].split()  
        if file_pairs[j] != '\n':
         if t_pairs[0] != "###":
           if t_pairs[0] != "No":
              A_atom1 = eval(str(t_bonds[2]))
              B_atom1 = eval(str(t_bonds[3]))
              A_ref = eval(str(t_pairs[3]))
              B_ref = eval(str(t_pairs[4]))
              if A_atom1-0.0001< A_ref <A_atom1+0.0001 and B_atom1-0.0001< B_ref <B_atom1+0.0001 :
                 atom1 = t_pairs[2]
              A_atom2 = eval(str(t_bonds[4]))
              B_atom2 = eval(str(t_bonds[5]))
              if A_atom2-0.0001< A_ref <A_atom2+0.0001 and B_atom2-0.0001< B_ref <B_atom2+0.0001 :
                 atom2 = t_pairs[2]
      file_out.write("%s %s %s %s\n"%tuple([t_bonds[0], t_bonds[1], atom1, atom2]))


