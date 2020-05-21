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
    file_angle_type = open(poly_name+"_angle_type_14.txt", "r").readlines()
    file_out = open(poly_name+"_angle_pair_coeff_15.txt", "w")

    for i in range(len(file_angle_type)):
      t_angles = file_angle_type[i].split()
      for j in range(len(file_pairs)):
        t_pairs = file_pairs[j].split()  
        #print t_angles[2], t_atoms[2] 
        if t_angles[2] == t_pairs[0]:
          A_atom1 = t_pairs[1]
          B_atom1 = t_pairs[2]
        if t_angles[3] == t_pairs[0]:
          A_atom2 = t_pairs[1]
          B_atom2 = t_pairs[2]
        if t_angles[4] == t_pairs[0]: 
          A_atom3 = t_pairs[1]
          B_atom3 = t_pairs[2]
      file_out.write("%s %s %s %s %s %s %s %s\n"%tuple([t_angles[0], t_angles[1], A_atom1, B_atom1, A_atom2, B_atom2, A_atom3, B_atom3]))


