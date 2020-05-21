import sys
import os
import math
from sys import argv, exit
#from pylab import *
import numpy
#import Scientific
#from Scientific.IO import ArrayIO
from string import split
import string
#from commands import cat

input_file1 = str(argv[1])  ###    coor file
f1 = open(input_file1, "r")
z1 = f1.readlines()

######### max atoms in mol 1 #############
atoms_mol_1 = int(argv[2])
######################################

for i in range(len(z1)):
    row1 = z1[i].split()
    if i < atoms_mol_1:
      mol_id = 1
    else:
      mol_id = 2    
    print str(row1[0]), mol_id, str(row1[2]), str(row1[3]), str(row1[4]), str(row1[5]), str(row1[6])
