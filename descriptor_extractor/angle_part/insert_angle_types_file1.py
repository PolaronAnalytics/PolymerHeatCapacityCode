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

    file_atoms = open(poly_name+"_part_atoms_8.txt", "r").readlines()
    file_angles = open(poly_name+"_part_angles_10.txt", "r").readlines()
    file_out = open(poly_name+"_angle_type_14.txt", "w")

    for i in range(len(file_angles)):
      t_angles = file_angles[i].split()
      for j in range(len(file_atoms)):
        t_atoms = file_atoms[j].split()  
        #print t_angles[2], t_atoms[2] 
        if t_angles[2] == t_atoms[0]:
          atom_1 = t_atoms[2]
        if t_angles[3] == t_atoms[0]:
          atom_2 = t_atoms[2]
        if t_angles[4] == t_atoms[0]: 
          atom_3 = t_atoms[2]
      file_out.write("%s %s %s %s %s\n"%tuple([t_angles[0], t_angles[1], atom_1, atom_2, atom_3]))


