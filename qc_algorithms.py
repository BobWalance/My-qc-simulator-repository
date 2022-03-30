
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

#3-24-2022 - 3 bit Grover's algorithms from
# https://www.nature.com/articles/s41467-017-01904-7
# This one doesn't have the ancillary qubit and is 'e'
#  in Fig.1 - Two-solution phase oracle marking the
#  |011> and |101> states.
# the final basis states don't match Fig.1 'e'
#  but the reversing the qubits version does.
# gates = [
# [ "h","C","i","h","x","C","x","h"],
# [ "h","i","C","h","x","C","x","h"],
# [ "h","z","z","h","x","z","x","h"]
# ]
# # reversed qubits - this matches Fig.1 'e'
# gates = [
# [ "h","z","z","h","x","z","x","h"],
# [ "h","i","C","h","x","C","x","h"],
# [ "h","C","i","h","x","C","x","h"]
# ]
#

# 3-26-2022 - Have split the initial Hadamard application and the repeating loop for Grovers.
#   13 qubits takes about 1/2 hour on the Raspberry Pi 4.
groversInit = [
["h"],
["h"],
#["h"],
#["h"],
#["h"],
#["h"],
#["h"],
#["h"],
#["h"],
["h"],
["h"],
["h"],
["h"]
]
groversGates = [
["O","h","x","C","x","h"],
["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
#["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","z","x","h"]
]


gates = [ # Bell state
[ "h","C"],
[ "i","i"],
[ "i","x"]
]



##############################################################################
# end of GATES list to be processed
##############################################################################
