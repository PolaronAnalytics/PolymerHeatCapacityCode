#!/bin/bash
#################################################################################################
#The software is developed by Rahul Bhowmik of Polaron Analytics 
#For any questions contact via email: rahulbhowmik@polaronanalytics.com or bhowmikrahul@gmail.com
#################################################################################################
#This software is distributed under the GNU General Public License.
#################################################################################################
mkdir folder_data
cp data* folder_data
#ls folder_data> file_names.txt
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/extract_info_file1.py  
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/nos_types_file2.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/comb_pair_tot_atoms_file3.py 
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/tot_atomic_types_file4.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/atomic_types_arranged_file5.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/combining_files_file6.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/insert_bond_types_file1.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/insert_bond_pair_coeff_file2.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/insert_angle_names_file3.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/bond_count_file4.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/bond_count_rem_dup_file5.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/*_file6.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/bond_part/*_file7.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/combine_bonds/*_file1.py


python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file1.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file2.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file3.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file4.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file5.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file6.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/angle_part/*file7.py

python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/combine_angles/*file1.py


python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file1.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file2.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file3.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file4.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file5.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file6.py
python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/dihedral_part/*file7.py

python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/combine_dihedrals/*file1.py

python2.7 /home/rahul/ml_project/jon/ML_Project/code_dev/python_files/test_dihedral.py
rm poly_* Poly* Nylon* PAS* polyethylene*
#####################################################################################

