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
import re

data_files = open("file_names.txt", "r").readlines()

for j in range(len(data_files)):
    name_spilt = data_files[j].split('.')
    poly_name = name_spilt[1].strip('\n')  
    f = open(data_files[j].strip('\n'), "r")
    #f = open(data_files[j].strip('\n'), "r")
    z = f.readlines()

#################################################################
##################### extracting nos ###########################
    file_out_1 = open(poly_name+"_part_nos_1.txt", "w")
    for i in range(1, len(z)):
      M = z[i]
      t = M.split()
      file_format_1 = "%s"
      line_tmp = [z[i]]
      if z[i] != '\n':
        if t[1]=="atom" and t[2]=="types":
          break
        file_out_1.write(file_format_1%tuple(line_tmp))

###################################################################
################# extracting total types ##########################
    file_out_1 = open(poly_name+"_part_types_2.txt", "w")
    for i in range(1, len(z)):
      M = z[i]
      t = M.split()
      file_format_1 = "%s"
      line_tmp = [z[i]]
      if z[i] != '\n':
        if len(t)==3: 
           if t[1]=="atom" or t[1]=="bond" or t[1]=="angle" or t[1]=="dihedral":
              file_out_1.write(file_format_1%tuple(line_tmp))
        if len(t)==4 and t[2]=="xlo" and t[3]=="xhi":
           break
#####################################################################
################# extracting masses #################################
    file_out_1 = open(poly_name+"_part_masses_3.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
        if t[0] == "Pair":
          break
        if t[0]=="Masses":
          k = i
        if i > k:
          file_format_1 = "%s"
          line_tmp = [z[i]]
          file_out_1.write(file_format_1%tuple(line_tmp))
################################################################
################### extracting pairs ###########################
    file_out_1 = open(poly_name+"_part_pairs_4.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
        if t[0] == "Bond":
          break
        if t[0]=="Pair":
          k = i
        if i > k:
          file_format_1 = "%s"
          line_tmp = [z[i]]
          file_out_1.write(file_format_1%tuple(line_tmp))
########################################################################
#################### extracting bond coefficients#######################
    file_out_1 = open(poly_name+"_part_bond_coeff_5.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
       if t[0] == "Angle":
         break
       if t[0]=="Bond":
         k = i
       if i > k:
         file_format_1 = "%s"
         line_tmp = [z[i]]
         file_out_1.write(file_format_1%tuple(line_tmp))
##################################################################
#################### extracting angles coeff ###########################
    file_out_1 = open(poly_name+"_part_angle_coeff_6.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
        if t[0] == "Dihedral":
           break
        if t[0]=="Angle":
           k = i
        if i > k:
           file_format_1 = "%s"
           line_tmp = [z[i]]
           file_out_1.write(file_format_1%tuple(line_tmp))
#############################################################
#################### extracting dihedrals coeff #######################
    file_out = open(poly_name+"_part_dihedral_coeff_7.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
       if t[0] == "Atoms":
         break
       if t[0]== "Dihedral":
         k = i
       if i > k:
         file_format_1 = "%s"
         line_tmp = [z[i]]
         file_out.write(file_format_1%tuple(line_tmp))

############################################################################
###################  extracting all the atoms #############################
    file_out_1 = open(poly_name+"_part_atoms_8.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
       if t[0] == "Bonds":
         break
       if t[0]=="Atoms":
         k = i
       if i > k:
         file_format_1 = "%s"
         line_tmp = [z[i]]
         file_out_1.write(file_format_1%tuple(line_tmp))
##############################################################################
###################  extracting all the bonds #############################
    file_out_1 = open(poly_name+"_part_bonds_9.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
       if t[0] == "Angles":
         break
       if t[0]=="Bonds":
         k = i
       if i > k:
         file_format_1 = "%s"
         line_tmp = [z[i]]
         file_out_1.write(file_format_1%tuple(line_tmp))
##############################################################################
################### extracting all the angles  ################################

    file_out_1 = open(poly_name+"_part_angles_10.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
        if t[0] == "Dihedrals":
          break
        if t[0]=="Angles":
          k = i
        if i > k:
          file_format_1 = "%s"
          line_tmp = [z[i]]
          file_out_1.write(file_format_1%tuple(line_tmp))
#####################################################################
#################extracting all the dihedrals  #############################
    file_out_1 = open(poly_name+"_part_dihedrals_11.txt", "w")
    k=10000000
    for i in range(len(z)):
      M = z[i]
      t = M.split()
      if z[i] != '\n':
        if t[0]=="Dihedrals":
          k = i
        if i > k:
          file_format_1 = "%s"
          line_tmp = [z[i]]
          file_out_1.write(file_format_1%tuple(line_tmp))
###########################################################################
###########################################################################
