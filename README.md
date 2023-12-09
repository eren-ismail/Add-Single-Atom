# Add-Single-Atom
Adds single atom with a specific distance to atom you chose for an xyz file.

Note 1: There is no distance conversion, so the distance is the same as your coordinates.
Note 2: Only works for XYZ file format.
Note 3: You have to know the order of atom. This can be checked via atomic visualization softwares. For example, when you click an atom in VESTA, you can learn its number. If you click a C atom, you can see the number in output window (Atom: 1 or Atom: 4)

Another way to check atom number is open the xyz file in an editor. If you substract 2 from the linenumber of that atom gives you the number.

## Usage
Let say that you want to add H atom to a C atom with a distance of 1.2 Angstrom at x & -0.5 at z directions. 
Let the C atom is the 54th atom in the structure.
And your structure file is let abc.xyz
First enter "abc"
Second enter "1.2 0.0 -0.5". Please also enter 0 for the distance you don't want to add.
Third enter "H"
New file will be created with name "abc_new.xyz"

### Author: Ismail Eren
