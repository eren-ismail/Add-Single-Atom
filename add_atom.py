# Author: Ismail Eren
# 
# Description: This is a simple script that adds single atom with a specific distance to atom you chose.
# Note 1: There is no distance conversion, so the distance is the same as your coordinates.
# Note 2: Only works for XYZ file format.
# Note 3: You have to know the order of atom. This can be checked via atomic visualization softwares. For example, when you click an
# atom in VESTA, you can learn its number. If you click a C atom, you can see the number in output window (Atom: 1 or Atom: 4)
# Another way to check atom number is open the xyz file in an editor. If you substract 2 from the linenumber of that atom gives you the number.
# For example, you want to add H atom to a C atom with a distance of 1.2 Angstrom at x & -0.5 at z directions. 
# Let the C atom is the 54th atom in the structure.
# And your structure file is let abc.xyz
# First enter "abc"
# Second enter "1.2 0.0 -0.5". Please also enter 0 for the distance you don't want to add.
# Third enter "H"
# New file will be created with name "abc_new.xyz"
import re

def add_distance(Atype, dx, dy, dz):
    # Code for adding distance to coordinates
    atom_number = int(input("Please Enter the Atom Number: "))
    atom_no_1 = atom_number + 2
  
    with open(f"{filename}.xyz", "r") as file:
        lines = file.readlines()
        total_atoms = int(lines[0].split()[0])

    new_total_atoms = total_atoms + 1
    with open(f"{filename}_new.xyz", "w") as new_file:
        new_file.write(f"{new_total_atoms}\n")
        new_file.writelines(lines[1: new_total_atoms + 1])

        pattern = re.compile(r'\s+')
        coordinates = pattern.split(lines[atom_no_1 - 1].strip())

        selected_atom_x = float(coordinates[1]) + dx
        selected_atom_y = float(coordinates[2]) + dy
        selected_atom_z = float(coordinates[3]) + dz

        new_file.write(f"{Atype}\t{selected_atom_x:.10f}\t{selected_atom_y:.10f}\t{selected_atom_z:.10f}\n")

# ...
filename = input("Please Enter the XYZ Filename (without extension): ")
distances = input("Please Enter the distances you want to add (x y z): ")
distances = distances.strip().split()
atomic_type = input("Please Enter the type of atom you want to add (H, O, S, C etc): ")
# usage
add_distance(atomic_type, float(distances[0]), float(distances[1]), float(distances[2]))


