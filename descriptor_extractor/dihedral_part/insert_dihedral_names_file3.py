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
    file_dihedral_pair = open(poly_name+"_dihedral_pair_coeff_18.txt", "r").readlines()
    file_out = open(poly_name+"_dihedral_name_19.txt", "w")

    for i in range(len(file_dihedral_pair)):
      t_dihedrals = file_dihedral_pair[i].split()
      for j in range(len(file_pairs)):
        t_pairs = file_pairs[j].split()  
        if file_pairs[j] != '\n':
         if t_pairs[0] != "###":
           if t_pairs[0] != "No":
              A_atom1 = eval(str(t_dihedrals[2]))
              B_atom1 = eval(str(t_dihedrals[3]))
              A_ref = eval(str(t_pairs[3]))
              B_ref = eval(str(t_pairs[4]))
              if A_atom1-0.0001< A_ref <A_atom1+0.0001 and B_atom1-0.0001< B_ref <B_atom1+0.0001 :
                 atom1 = t_pairs[2]
              A_atom2 = eval(str(t_dihedrals[4]))
              B_atom2 = eval(str(t_dihedrals[5]))
              if A_atom2-0.0001< A_ref <A_atom2+0.0001 and B_atom2-0.0001< B_ref <B_atom2+0.0001 :
                 atom2 = t_pairs[2]
              A_atom3 = eval(str(t_dihedrals[6]))
              B_atom3 = eval(str(t_dihedrals[7]))
              if A_atom3-0.0001< A_ref <A_atom3+0.0001 and B_atom3-0.0001< B_ref <B_atom3+0.0001 :
                 atom3 = t_pairs[2]

              A_atom4 = eval(str(t_dihedrals[8]))
              B_atom4 = eval(str(t_dihedrals[9]))
              if A_atom4-0.0001< A_ref <A_atom4+0.0001 and B_atom4-0.0001< B_ref <B_atom4+0.0001 :
                 atom4 = t_pairs[2]

              #break 
      #print t_dihedrals[0], t_dihedrals[1], atom1, atom2, atom3
      file_out.write("%s %s %s %s %s %s\n"%tuple([t_dihedrals[0], t_dihedrals[1], atom1, atom2, atom3, atom4]))


