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

    file_nos = open(poly_name+"_part_nos_1.txt", "r").readlines()
    file_types = open(poly_name+"_part_types_2.txt", "r").readlines()
    file_out = open(poly_name+"_nos_types.txt", "w")

    ATOM_NOS=[]
    BOND_NOS=[]
    ANGLE_NOS=[]
    DIHEDRAL_NOS=[]

    ATOM_TYPES=[]
    BOND_TYPES=[]
    ANGLE_TYPES=[]
    DIHEDRAL_TYPES=[]

    for i in range(len(file_nos)):
     t_nos = file_nos[i].split()
     #file_format_1 = "%s"
     if len(t_nos) > 1:
       if t_nos[1]=="atoms":
         ATOM_NOS.append(t_nos[0])
       if t_nos[1]=="bonds":
         BOND_NOS.append(t_nos[0])
       if t_nos[1]=="angles":
         ANGLE_NOS.append(t_nos[0])
       if t_nos[1]=="dihedrals":
         DIHEDRAL_NOS.append(t_nos[0])

    for i in range(len(file_types)):
     t_types = file_types[i].split()
     #file_format_1 = "%s"
     if len(t_types) > 1:
       if t_types[1]=="atom":
         ATOM_TYPES.append(t_types[0])
       if t_types[1]=="bond":
         BOND_TYPES.append(t_types[0])
       if t_types[1]=="angle":
         ANGLE_TYPES.append(t_types[0])
       if t_types[1]=="dihedral":
         DIHEDRAL_TYPES.append(t_types[0])


    file_out.write("%s %s %s %s %s %s %s %s\n"%tuple(["total_atoms", "total_bonds", "total_angles", "total_dihedrals", "total_atom_types", "total_bond_types", "total_angle_types", "total_dihedral_types"]))

    file_out.write("%s %s %s %s %s %s %s %s\n"%tuple([ATOM_NOS[0], BOND_NOS[0], ANGLE_NOS[0], DIHEDRAL_NOS[0], ATOM_TYPES[0], BOND_TYPES[0], ANGLE_TYPES[0], DIHEDRAL_TYPES[0]]))


