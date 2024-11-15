
##############################################################################
# GATES list to be processed (start)
##############################################################################
#
# The zero'th qubit is the top row
# Each column is one gate time for all qubits
# Only one controlled gate per gate time is allowed (for now)
# Put an "i" (identity matrix) for each unaffected qubit gate time
# 10 qubits is the most allowed (11 and 12 qubits cause a strange error sometimes and 13 is Numpy's max)
#
# gates = [
# [ "h","h"],
# [ "i","h"]
# ]
# gates = [
# [ "x",'x'],
# [ "h",'i']
# ]
# gates = [
# [ "h","h"],
# [ "i","i"]
# ]
# gates = [
# [ "y","i"],
# [ "i","i"]
# ]
# gates = [
# [ "h","C"],
# [ "i","x"],
# [ "h","i"]
# ]
# gates = [ # Bell state
# [ "h","C"],
# [ "i","x"]
# ]
# 
# # let's try 10 gubits
# gates = [
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"]
# ]
# # let's try 13 gubits
# gates = [
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"],
# [ "h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h","h"]
# ]
# # let's try 15 gubits
# gates = [
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"]
# ]
# # let's try 13 gubits (14 gave error) -- 13 is the max number of qubits
# gates = [
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"],
# [ "h","h"]
# ]
# # let's try 13 gubits (14 gave error) -- 13 is the max number of qubits
# gates = [
# [ "h","C"],
# [ "i","x"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"]
# ]
# gates = [ # when I add 8 more qubits of"i" it fails, but this works
# [ "h","C"],
# [ "i","x"],
# [ "i","i"]
# ]
# gates = [ # when I add ? more qubits of"i" it fails, but this works
# [ "h","C"],
# [ "i","x"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"], # qubit 10
# [ "i","i"] # this 11th qubit caused failure (name "C" is not defined
# ]

# 5-27-2021 - CHECK THIS against IBM (if possible). Why do I show qubit 5 entangled?
# gates = [ # when I add ? more qubits of"i" it fails, but this works
# [ "h","C"],
# [ "i","x"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "h","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"],
# [ "i","i"] # qubit 10 (this is the max number of qubits with C -- 11 qubits fails)
# ]
# # gates = [
# # [ "h","C"],
# # [ "x","x"]
# # ]
# gates = [
# [ "h","C","i","y","C"],
# [ "i","x","C","i","i"],
# [ "i","i","x","i","x"]
# ]
# gates = [ # This circuit, according to the IBM simulator, entangles all three qubits with evenly-split probablities over the 8 basis states
# [ "h","C","i","i"],
# [ "i","x","x","h"],
# [ "h","i","C","i"]
# ]

# gates = [
# [ "i","i"],
# [ "i","i"]
# ]
# produces this final stateVector:
# array([ 0.35355339,  0.35355339,  0.35355339, -0.35355339,  0.35355339,
#         0.35355339, -0.35355339,  0.35355339])

# gates = [
# [ "h"],
# [ "h"],
# [ "h"]
# ]
# three Hadamard gates produces this final stateVector:
# array([0.35355339, 0.35355339, 0.35355339, 0.35355339, 0.35355339,
#        0.35355339, 0.35355339, 0.35355339])


# gates = [
# [ "h","C"],
# [ "i","x"],
# [ "h","i"],
# [ "h","i"],
# [ "h","i"],
# [ "h","i"],
# [ "h","i"],
# [ "h","i"]
# ]
# 
# gates = [
# [ "h","C"],
# [ "i","i"],
# [ "i","x"]
# ]

# gates = [ # Bell state
# [ "h","C"],
# [ "i","x"]
# ]

# gates = [ # Entanglement on qubits 0,2 and 3
# [ "h","C","i","i"],
# [ "i","i","i","i"],
# [ "i","x","x","h"],
# [ "h","i","C","i"]
# ]

# gates = [
# [ "h","C","i"],
# [ "i","x","i"],
# [ "h","i","i"] # DON'T put anything else in gate time 1 (where the controlled qubit is
# ]

# 3-20-2022 - testing the cz (controlled z) gate
# gates = [
# [ "h","C"],
# [ "i","i"],
# [ "i","z"]
# ]
# gates = [
# [ "i","C"],
# [ "i","z"]
# ]
# gates = [
# [ "i","i"],
# [ "i","C"],
# [ "i","z"]
# ]
# gates = [
# [ "i","C"],
# [ "i","z"],
# [ "i","i"],
# [ "i","i"]
# ]
# gates = [
# [ "i","i"],
# [ "i","i"],
# [ "i","C"],
# [ "i","z"]
# ]

# Grover's algorithm (N=2,A=00)
# note that the "phase gate" 'p' is labeled as 's' on IBM's quantum-computing.ibm.com site (either will work here)
# gates = [
# [ "h","p","C","p","h","x","C","x","h"],
# [ "h","p","z","p","h","x","z","x","h"]
# ]

# 3-23-2022 - testing multiple control gates
# gates = [
# [ "i","C"],
# [ "i","z"],
# [ "i","C"],
# [ "i","C"]
# ]
# gates = [
# [ "C"],
# [ "z"],
# [ "C"]
# ]
# gates = [
# [ "i"],
# [ "z"],
# [ "C"],
# [ "C"]
# ]
# gates = [ # this worked
# [ "C"],
# [ "z"]
# ]
# gates = [ # this worked
# [ "z"],
# [ "C"]
# ]

# gates = [
# [ "C"],
# [ "x"]
# ]
# gates = [
# [ "x"],
# [ "C"]
# ]
# gates = [
# [ "i"],
# [ "x"],
# [ "C"]
# ]
# gates = [
# [ "C"],
# [ "x"],
# [ "C"],
# [ "C"]
# ]

# 
# gates = [ # Bell state
# [ "h","C"],
# [ "i","i"],
# [ "i","x"]
# ]
# 
# gates = [ # 4-3-2022 testing
# [ "i","y"],
# [ "i","i"],
# [ "i","i"]
# ]
# 
# gates = [ # 4-3-2022 testing
# [ "x","p4"]
# ]
# gates = [ # 4-4-2022 testing
# [ "i","i"],
# [ "x","p4"]
# ]
# gates = [ # 4-4-2022 testing
# [ "x","C"],
# [ "i","p4"]
# ]
# gates = [ # 4-4-2022 testing
# [ "i","C"],
# [ "x","p4"]
# ]
# gates = [ # 4-4-2022 testing
# [ "h","C"],
# [ "i","p4"]
# ]
# gates = [ # 4-4-2022 testing
# [ "i","p4"],
# [ "h","C"]
# ]
# gates = [ # 4-3-2022 testing
# [ "x","p4"]
# ]
# gates = [ # 4-3-2022 testing
# [ "x","p4"],
# [ "x","C"]
# ]


# gates = [ # 4-4-2022 first test of the quantum Fourier transform
# [ "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-4-2022 Creating a bit pattern in the first gate time - first test of the quantum Fourier transform
# [ "i",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "i",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "i",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "x",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "x",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on all qubits. This results in 1 for basis state 00000
# [ "h",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "h",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "h",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "h",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "h",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on all qubits followed by various gates. This is interesting.
# [ "h","i",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "i","i",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"], # "z","y","h","s","p2","p4","p8","p16" after the first "h" produces results. "p16" much less than "p2". "x" does not.
# [ "i","i",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "h","i",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "h","i",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on all qubits followed by various gates. This is interesting.
# [ "h","i",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "h","s",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"], # "z","y","h","s","p2","p4","p8","p16" after the first "h" produces results. "p16" much less than "p2". "x" does not.
# [ "h","i",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "h","i",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "h","i",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on some of the qubits followed by various gates.
# [ "h",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "h",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "h",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "i",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "i",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on some of the qubits.
# [ "i",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "i",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "h",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "h",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "h",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on some of the qubits.
# [ "i",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "h",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "h",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "h",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "h",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on some of the qubits.
# [ "i",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "h",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "i",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "h",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "i",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]
# gates = [ # 4-5-2022 Using initial Hadamard on some of the qubits.
# [ "h",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
# [ "i",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
# [ "h",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
# [ "i",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
# [ "h",  "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
# ]

# gates = [ # one-qubit QFT
# ["x","h",    "h"] # "h","h", "h" yields 1.0|0> + 0.0|1> while "x","h", "h" yields  0.0|0> + 1.0|1>
# ]

# gates = [ # 4-8-2022 Using 0's ("i") and 1's ("x") as input and doing a final Hadamard on all qubits. It is different and interesting.
# [ "x",  "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i",  "h"],
# [ "x",  "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i",  "h"],
# [ "x",  "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i",  "h"],
# [ "x",  "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i",  "h"],
# [ "x",  "i","i", "i","i", "i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h",  "h"]
# ]

# gates = [ # 4-8-2022 REARRANGE - Using 0's ("i") and 1's ("x") as input and doing a final Hadamard on all qubits. It is different and interesting.
# [ "i",  "h","p2","p4","p8","p16",  "i","-", "-", "-",   "i","-", "-",   "i","-",   "i",    "h"],
# [ "i",  "i","C", "-", "-", "-",    "h","p2","p4","p8",  "i","-", "-",   "i","-",   "i",    "h"],
# [ "x",  "i","-", "C", "-", "-",    "i","C", "-", "-",   "h","p2","p4",  "i","-",   "i",    "h"],
# [ "i",  "i","-", "-", "C", "-",    "i","-", "C", "-",   "i","C", "-",   "h","p2",  "i",    "h"],
# [ "i",  "i","-", "-", "-", "C",    "i","-", "-", "C",   "i","-", "C",   "i","C",   "h",    "h"]
# ]
# 
# gates = [ # 4-8-2022 REARRANGE - Using 0's ("i") and 1's ("x") followed by Hadamards at the input.
# [ "i","h",  "h","p2","p4","p8","p16",  "i","-", "-", "-",   "i","-", "-",   "i","-",   "i"],
# [ "i","h",  "i","C", "-", "-", "-",    "h","p2","p4","p8",  "i","-", "-",   "i","-",   "i"],
# [ "x","h",  "i","-", "C", "-", "-",    "i","C", "-", "-",   "h","p2","p4",  "i","-",   "i"],
# [ "x","h",  "i","-", "-", "C", "-",    "i","-", "C", "-",   "i","C", "-",   "h","p2",  "i"],
# [ "x","h",  "i","-", "-", "-", "C",    "i","-", "-", "C",   "i","-", "C",   "i","C",   "h"]
# ]
# 
# 
# gates = [ # 4-9-2022 testing
# ["h","p4"]
# ]
# gates = [ # 4-9-2022 testing
# ["i"]
# ]


# gates = [ # 4-9-2022 - Inverse quantum Fourier transform
# [ "i",   "p-2","p-4","p-8","p-16","h",   "-",  "-",  "-",  "i",    "-",  "-",  "i",   "-",  "i",   "i"],
# [ "i",   "C",  "-",  "-",  "-",   "i",   "p-2","p-4","p-8","h",    "-",  "-",  "i",   "-",  "i",   "i"],
# [ "x",   "-",  "C",  "-",  "-",   "i",   "C",  "-",  "-",  "i",    "p-2","p-4","h",   "-",  "i",   "i"],
# [ "x",   "-",  "-",  "C",  "-",   "i",   "-",  "C",  "-",  "i",    "C",  "-",  "i",   "p-2","h",   "i"],
# [ "x",   "-",  "-",  "-",  "C",   "i",   "-",  "-",  "C",  "i",    "-",  "C",  "i",   "C",  "i",   "h"]
# ]
# 
# gates = [ # 4-9-2022 - This might be closer to Shor implemenation - but for the quantum modular exponentiation phase kickback causing the initial rotations (after the first Hadamards)
# [ "h","p1",    "p-2","p-4","p-8","p-16","h",   "-",  "-",  "-",  "i",    "-",  "-",  "i",   "-",  "i",   "i"],
# [ "h","p1",    "C",  "-",  "-",  "-",   "i",   "p-2","p-4","p-8","h",    "-",  "-",  "i",   "-",  "i",   "i"],
# [ "h","p1",    "-",  "C",  "-",  "-",   "i",   "C",  "-",  "-",  "i",    "p-2","p-4","h",   "-",  "i",   "i"],
# [ "h","p1",    "-",  "-",  "C",  "-",   "i",   "-",  "C",  "-",  "i",    "C",  "-",  "i",   "p-2","h",   "i"],
# [ "h","p1",    "-",  "-",  "-",  "C",   "i",   "-",  "-",  "C",  "i",    "-",  "C",  "i",   "C",  "i",   "h"]
# ]
# 
# gates = [ # 4-9-2022 - UPSIDE-DOWN - This might be closer to Shor implemenation - but for the quantum modular exponentiation phase kickback causing the initial rotations (after the first Hadamards)
# [ "h","p2",    "-",  "-",  "-",  "C",   "i",   "-",  "-",  "C",  "i",    "-",  "C",  "i",   "C",  "i",   "h"],
# [ "h","p2",    "-",  "-",  "C",  "-",   "i",   "-",  "C",  "-",  "i",    "C",  "-",  "i",   "p-2","h",   "i"],
# [ "h","p2",    "-",  "C",  "-",  "-",   "i",   "C",  "-",  "-",  "i",    "p-2","p-4","h",   "-",  "i",   "i"],
# [ "h","p2",    "C",  "-",  "-",  "-",   "i",   "p-2","p-4","p-8","h",    "-",  "-",  "i",   "-",  "i",   "i"],
# [ "h","p2",    "p-2","p-4","p-8","p-16","h",   "-",  "-",  "-",  "i",    "-",  "-",  "i",   "-",  "i",   "i"]
# ]
# 
# gates = [ # 4-9-2022 - Implementing SWAP gates with 3xCNOT. This might be closer to Shor implemenation - but for the quantum modular exponentiation phase kickback causing the initial rotations (after the first Hadamards)
# [ "h","p1",    "p-2","p-4","p-8","p-16","h",   "-",  "-",  "-",  "i",    "-",  "-",  "i",   "-",  "i",   "i",  "x","C","x", "-","-","-"],
# [ "h","p1",    "C",  "-",  "-",  "-",   "i",   "p-2","p-4","p-8","h",    "-",  "-",  "i",   "-",  "i",   "i",  "-","-","-", "x","C","x"],
# [ "h","p1",    "-",  "C",  "-",  "-",   "i",   "C",  "-",  "-",  "i",    "p-2","p-4","h",   "-",  "i",   "i",  "-","-","-", "-","-","-"],
# [ "h","p1",    "-",  "-",  "C",  "-",   "i",   "-",  "C",  "-",  "i",    "C",  "-",  "i",   "p-2","h",   "i",  "-","-","-", "C","x","C"],
# [ "h","p1",    "-",  "-",  "-",  "C",   "i",   "-",  "-",  "C",  "i",    "-",  "C",  "i",   "C",  "i",   "h",  "C","x","C", "-","-","-"]
# ]

# RBW 4-15-2022
# For two qubits, these initializations will create an initial state vector (the input to the QFT) that results in a final state probabilities (the output of the QFT)
# Initial qubit gates -- Initial state vector -- Final state probabilities
#      "i"                [1, 0]                       [0.25, 0.25, 0.25, 0.25]
#      "i"
#
#      "h"                [0.707, 0, 0.707, 0]         [0.5, 0, 0.5, 0]  THIS ISN"T WORKING
#      "i"
#
#      "h"                [0.707, 0.707, 0.707, 0.707] [1, 0, 0, 0]
#      "h"

# gates = [ # 4-15-2022 -  QFT4 with swap gate)
# [ "h",   "h","p2","i",  "C","x","C"],
# [ "i",   "i","C", "h",  "x","C","x"]
# ]
# gates = [ # 4-15-2022 -  QFT4 with swap gate)
# [ "h",   "h","p2","i",  "x","C","x"],
# [ "i",   "i","C", "h",  "C","x","C"]
# ]
# 
# #testing the swap
# gates = [ # 4-15-2022 -  QFT4 with swap gate)
# [ "h", "x","C","x"],
# [ "i", "C","x","C"]
# ]
# 
# gates = [ # 4-15-2022 -  QFT4 with swap gate)
# [ "i", "x","C","x"],
# [ "h", "C","x","C"]
# ]
# gates = [ # 4-15-2022 - this creates 1100, but why?
# [ "h"],
# [ "i"]
# ]
# gates = [ # 4-15-2022 - this creates 1010, but why?
# [ "i"],
# [ "h"]
# ]
# 
gates = [ # 4-15-2022 -  QFT4 without swap gate TESTING by forcing an initial stateVector of 1010
[ "h","p2","i"],
[ "i","C", "h"]
]


gates = [ # 4-15-2022 - QFT4 with swap gate TESTING by forcing an initial stateVector of 1010 (0.707,0,0.707,0). THIS NOW WORKS AFTER REVKRON.
[ "h","p2","i",  "x","C","x"],
[ "i","C", "h",  "C","x","C"]
]
gates = [ # 4-16-2022 - QFT4 with swap gate. REVERSED QUBIT ORDER (top -> bottom qubit swap) by forcing an initial stateVector of 1010 (0.707,0,0.707,0). KRON order back to stock to meet 'IBM's qubit 0 on the top'.
[ "i","C", "h",  "C","x","C"],
[ "h","p2","i",  "x","C","x"]
]

gates = [ # 4-16-2022 REARRANGE - QFT32 with swap gates at the end.
["i","-", "-", "-", "C",    "i","-", "-", "C",   "i","-", "C",   "i","C",   "h",  "C","x","C",  "-","-","-"],
["i","-", "-", "C", "-",    "i","-", "C", "-",   "i","C", "-",   "h","p2",  "i",  "-","-","-",  "C","x","C"],
["i","-", "C", "-", "-",    "i","C", "-", "-",   "h","p2","p4",  "i","-",   "i",  "-","-","-",  "-","-","-"],
["i","C", "-", "-", "-",    "h","p2","p4","p8",  "i","-", "-",   "i","-",   "i",  "-","-","-",  "x","C","x"],
["h","p2","p4","p8","p16",  "i","-", "-", "-",   "i","-", "-",   "i","-",   "i",  "x","C","x",  "-","-","-"]
]



# gates = [ # Bell state
# [ "h","C"],
# [ "i","i"],
# [ "i","x"]
# ]
# gates = [ # Bell state
# [ "h","C"],
# [ "i","x"]
# ]
# gates = [ # Bell state
# [ "h","x"],
# [ "i","C"]
# ]
# gates = [ # 4-16-2022 Testing qubit to basis state order. Since reversing the KRON arguments, the top qubit now affects basis state 4. WRONG.
# [ "x"],
# [ "i"],
# [ "i"]
# ]


# 4-28-2022 - testing MEASURE
gates = [ # Bell state
[ "h","C"],
[ "i","x"]
]

gates = [ # 5-4-2022 - Testing the 't' gate
["x","t"]
]

# gates = [ # 5-4-2022 - Testing the 't' gate
# ["h"],
# ["i"]
# ]



# 6-20-2022 - looking at entanglement
gates = [ # Bell state
[ "h","C"],
[ "i","x"]
]
##    entanglementValue for qubit 0  =  (0.5+0j)
##    entanglementValue for qubit 1  =  (0.5+0j)
##    final stateVector (not Grover's algorithm)=
##     [[0.70710678+0.j]
##     [0.        +0.j]
##     [0.        +0.j]
##     [0.70710678+0.j]]

### 6-20-2022 - looking at entanglement
##gates = [
##[ "h"],
##[ "h"]
##]
##    entanglementValue for qubit 0  =  1.0
##    entanglementValue for qubit 1  =  1.0
##    final stateVector (not Grover's algorithm)=
##     [[0.5]
##     [0.5]
##     [0.5]
##     [0.5]]

### 6-20-2022 - looking at entanglement
##gates = [ #
##[ "h","C"],
##[ "i","z"]
##]
##    entanglementValue for qubit 0  =  (1+0j)
##    entanglementValue for qubit 1  =  (1+0j)
##    final stateVector (not Grover's algorithm)=
##     [[0.70710678+0.j]
##     [0.70710678+0.j]
##     [0.        +0.j]
##     [0.        +0.j]]


# 6-20-2022 - looking at entanglement
gates = [ # Bell state (top two qubits only)
[ "h","C"],
[ "i","x"],
[ "i","i"]
]
##    entanglementValue for qubit 0  =  (0.5+0j)
##    entanglementValue for qubit 1  =  (0.5+0j)
##    entanglementValue for qubit 2  =  (1+0j)
##    final stateVector (not Grover's algorithm)=
##     [[0.70710678+0.j]
##     [0.        +0.j]
##     [0.        +0.j]
##     [0.70710678+0.j]
##     [0.        +0.j]
##     [0.        +0.j]
##     [0.        +0.j]
##     [0.        +0.j]]


# 9-13-2024 - 2 entangled qubits
#gates = [ # Bell state
#[ "h","C"],
#[ "i","x"]
#]
## 

# 9-13-2024 - 2 qubits with Hadamards
#gates = [
#[ "h"],
#[ "h"]
#]
##


gates = [ # 4-4-2022 first test of the quantum Fourier transform
[ "h","p2","i","p4","i", "i", "i", "p8","i", "p16","i", "i","i", "i", "i"],
[ "i","C", "h","i", "p2","i", "p4","i", "p8","i",  "i", "i","i", "i", "i"],
[ "i","i", "i","C", "C", "h", "i", "i", "i", "i",  "p2","i","i", "p4","i"],
[ "i","i", "i","i", "i", "i", "C", "C", "i", "i",  "C", "h","p2","i", "i"],
[ "i","i", "i", "i","i", "i", "i", "i", "C", "C",  "i", "i","C", "C", "h"]
]

# 9-13-2024 - I'm surprised that this doesn't end up with any entanglement since
#  there are Hadamard followed by CNOT, but perhaps they cancel themselves out.
gates = [ # 4-16-2022 REARRANGE - QFT32 with swap gates at the end.
["i","-", "-", "-", "C",    "i","-", "-", "C",   "i","-", "C",   "i","C",   "h",  "C","x","C",  "-","-","-"],
["i","-", "-", "C", "-",    "i","-", "C", "-",   "i","C", "-",   "h","p2",  "i",  "-","-","-",  "C","x","C"],
["i","-", "C", "-", "-",    "i","C", "-", "-",   "h","p2","p4",  "i","-",   "i",  "-","-","-",  "-","-","-"],
["i","C", "-", "-", "-",    "h","p2","p4","p8",  "i","-", "-",   "i","-",   "i",  "-","-","-",  "x","C","x"],
["h","p2","p4","p8","p16",  "i","-", "-", "-",   "i","-", "-",   "i","-",   "i",  "x","C","x",  "-","-","-"]
]


# 9-14-2024 - 3 qubits with two entangled. The first qubit is not entangled
gates = [
[ "i","i"],
[ "h","C"],
[ "i","x"]
]
## 
# 9-14-2024 - 3 qubits with two entangled. The last qubit is not entangled
gates = [
[ "h","C"],
[ "i","x"],
[ "i","i"]
]
##


# 9-14-2024 - 3 qubits with two entangled with the one in the middle not entangled
gates = [
[ "h","C"],
[ "i","i"],
[ "i","x"]
]
## 

# 9-16-2024 - 3 qubits with 3 identity matrices
gates = [
[ "i"],
[ "i"],
[ "i"],
[ "i"]
]
## 

# 9-14-2024 - 3 qubits with two entangled. The first qubit is not entangled
gates = [
[ "i","i"],
[ "h","C"],
[ "i","x"]
]
## 




# 9-20-2024 - entangled qubits - this DOESN'T match IBM
#   BECAUSE my code doesn't allow for two CNOT gates in the same gate time.
gates = [ # Bell state
[ "h","C"],
[ "i","x"],
[ "h","C"],
[ "i","x"]
]
## 
# 9-20-2024 - entangled qubits - this DOES match IBM
gates = [ # Bell state
[ "h","C","i","i"],
[ "i","x","i","i"],
[ "i","i","h","C"],
[ "i","i","i","x"]
]
## 


# 9-20-2024 - 3 qubits with Hadamards and controls on the first two qubits. The third qubit is a controlled NOT.
#  IBM gives "Reduced purity" of 0.5,0.5,0.25 for this circuit. I don't.
gates = [
[ "h","C"],
[ "h","C"],
[ "i","x"]
]
## 
# 9-20-2024 - TESTING ABOVE circuit - 3 qubits with Hadamards and controls on the first two qubits. The third qubit is a controlled NOT.
gates = [
[ "h","C","i","i"],
[ "i","i","h","C"],
[ "i","x","i","x"]
]
##


 
# 9-20-2024 - entangled qubits - this DOES match IBM
gates = [ # Bell state
[ "h","C","i","i"],
[ "i","x","i","i"],
[ "i","i","h","C"],
[ "i","i","i","x"]
]
## 




# 10-6-2024 - 3 qubits with two entangled. The first qubit is not entangled
gates = [
[ "i","i"],
[ "h","C"],
[ "i","x"]
]
##




# 10-6-2024 - 3 qubits with Hadamards and controls on the first two qubits. The third qubit is a controlled NOT.
#  IBM gives "Reduced purity" of 0.625,0.625,0.625 for this circuit. So do I.
gates = [
[ "h","C"],
[ "h","C"],
[ "i","x"]
]
##


# 10-6-2024 - 2 entangled qubits
gates = [ # Bell state
[ "h","C"],
[ "i","x"]
]
##

# 10-23-2024 - Creating lopsided probabilites with "h" "t" "h"
gates = [

[ "i","i","h","C"],
[ "h","t","h","x"]
]
##



##############################################################################
# end of GATES list to be processed
##############################################################################
