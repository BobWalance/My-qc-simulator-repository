# RBW - 9-13-2024 - Calling MyCalculateAndDisplayQubitsEntanglement() instead of CalculateAndDisplayQubitsEntanglement()
#                    so that ptrace_outer is no longer needed.
# RBW - 6-21-2022 - Implemented ptrace_outer locally in qc_functions.py rather than depending on 'from partial_trace_from_statevector import ptrace_outer'.
#                   Qutip no longer required.
# RBW - 6-11-2022 - Displaying histograms for Grovers initialized and first Hadamarized states.
# RBW - 5-15-2022 - Printing the number of qubits as the Grovers measurements proceed.
# RBW - 5-14-2022 - Added ability for user to select how many qubits are involved in Grovers algorithm.
# RBW - 5-13-2022 - Grover's algorithm now only plots the histogram of the measurements.
# RBW - 5-12-2022 - Histograms for the Grover's measurements are now shown when not plotting the calculated probabilities.
# RBW - 5-07-2022 - Simplified call to Grovers. User input prompt to continue Grover's looping fixed.
# RBW - 5-06-2022 - Cleaned up a bit more. Moved the Grover's gates to qc_grovers.py. Created separate qc_grovers.py and qc_functions.py files.
# RBW - 5-04-2022 - Added the T gate to qc_simple_gates.py.
# RBW - 5-01-2022 - Improved the output text for Grover's.
# RBW - 4-30-2022 - Added ability to show simulated basis-state measurements.
# RBW - 4-16-2022 - QFT32 results look correct when using 1's and 0s within their forced initial state vectors.
#                   The IBM simulator has qubit 0 on the top. I've put the KRON arguments order back to original so that my qubit 0 is at the top as IBM's is.
#                   To make the QFT work, I had to reverse the qubit order top-to-bottom. Now all is well with other types of gates, too.
#                   Needs cleanup.
# RBW - 4-15-2022 - Reversing all the KRON arguments. This broke the qubit order with respect to the IBM simulator.
#                   Working on the QFT4 and various input vectors.
# RBW - 4-9-2022 -  Implemented SWAP gates with 3xCNOT gates in qc_algorithms.py.
#                   Added 5 qubit inverse Quantum fourier transform to qc_algorithms.py. Still have equal superposition with iixxi type inputs (no surprise).
# RBW - 4-8-2022 -  Rearranged the QFT gates to make it easier to read and to expand to more qubits.
# RBW - 4-5-2022 -  Creating an initial qubit pattern and observing results on the 5 qubit QFT. ihhhh and hiiii are interesting.

# RBW - 4-4-2022 -  Trying a quantum Fourier transform with 5 qubits. This results in equal probabilities on all basis states.
# RBW - 4-4-2022 -  The controlled "px" gate seems to be working.
# RBW - 4-3-2022 -  Having trouble feeding phasePiDivisor to the generic "px" gate that was in qc_simple_gates. Had to create it where needed.
# RBW - 4-3-2022 -  Starting work on Shor's algorithm. Adding phase gates needed for the quantum Fourier transform.
# RBW - 3-30-2022 - This version shared on physicsforums.com.
# RBW - 3-29-2022 - Added ability for user to select Grover's or other algorithm.
# RBW - 3-28-2022 - Made the plot size larger. Displaying the qubits entanglements for all stages of Grover's algorithm.
# RBW - 3-27-2022 - Plotting stateVector probabilities after each stage of Grover's.
# RBW - 3-26-2022 - Added looping for Grover's.
#                   Added code to create the Grover's oracle matrix automatically. It's working with 11 qubits (haven't tried more).
#                   Files split for readability. There are four files now in this project.
#                   The targetQubit and items in the controlQubits list are now zero-based as they really are.
# RBW - 3-25-2022 - Looping the Grover's 'Oracle and amplification' sections. It really works to boost the found basis state's probability.
#                   Converted several while loops into for loops for code reduction. Now printing the stateVector after each gate time.
#                   Doing up to 5 qubits for Grover's. Have added my own evolving matrix 'M' for use in testing Grover's algorithm.
# RBW - 3-24-2022 - Trying the 3 qubit Grover's algorithm from https://www.nature.com/articles/s41467-017-01904-7.
# RBW - 3-24-2022 - Multiple-control cnot gate and cz gate seems to be working.
# RBW - 3-23-2022 - Updated using the list of control qubits.
# RBW - 3-20-2022 - Adding simple Grover's Algorithm.
# RBW - 6-15-2021 - Modified so that the stateVector became a true vector (nx1) and not an 'array'.
# RBW - 5-28-2021 - Fixed 'wrong entanglement value bug'.
#                   Used dot product instead of simple '*' for squaring of the partial traces.
# RBW - 5-27-2021 - Printing out the entanglement values for all qubits.
# RBW - 5-26-2021 - I am trying user "slek120" code from scicomp.stackexchange.com - question 30052. It think it's (almost) working!
# RBW - 5-25-2021 - Adding qutip to do the partial tracing for entanglement measure calculations.
# RBW - 5-20-2021 - Cleaned up a bit.
# RBW - 5-18-2021 - I think that I've successfully created the density matrix from the stateVector.
# RBW - 5-12-2021 - Switched to bar graph plot for solid vertical lines for each probability magnitude.
#                   Changed the state vector name from'v' to 'stateVector'.
# RBW - 5-11-2021 - Adding plotting of the probability amplitudes.
#                   Controlled gates (only type 'x' so far seems to work.
#                   Had to return empty np.array if a
#                    controlled gate not found in the current gate time.
# RBW - 5-10-2021 - Adding the controlled-gate handler.
# RBW - 5-7-2021 - Had the tensor (kronecker) product arguments reversed. Added x,y,z,p gates.
# RBW - 5-6-2021 - qc_sim_1.py
#  This is the top-level quantum computer simulator file
import numpy as np
import matplotlib.pyplot as plt

from qc_controlled_gates import *
from qc_simple_gates import *
from qc_algorithms import *
from qc_grovers import *
from qc_functions import *
#
# Notes on Python lists
# 2D list example (use this format for multi-qubit gates list):
# test = [
# [ "1", "2", "3", "4"],
# [ "5", "6", "7", "8"],
# [ "9","10","11","12"]
# ]
# operations on this list:
# len(test) -> 3 (i.e., the number of rows in the list)
# len(test[0]) -> 4 (i.e., the number of columns in the list)
# len(test[1]) -> 4 (i.e., the number of columns in the list)
# len(test[2]) -> 4 (i.e., the number of columns in the list)
# len(test[3]) -> ERROR (there are only 3 rows to chose from
# len(test[]) -> ERROR
# test[1][2] -> 7 (i.e., test[row][col]
#
# 1D list example (use this format for single qubit gates list):
# test = [
# [ "1", "2", "3", "4"]
# ]
# len(test) -> 1 (only one row in this list)
# len(test[0]) -> 4 (four columns)
# test[0][2] -> 3 (i.e., test[row][col]
#
#
############################
# GLOBAL VARIABLES
############################
measurementShots = 100 # the number of measurements to perform
#
####################################################################################
#                         MAIN CODE
####################################################################################
print ("Processing started...")
#
userInput = input("Do Grover's algorithm? (ENTER for YES, or 'any key'+ ENTER for NO)")
if userInput == "":
    runGroversAlgorithm = True
else:
    runGroversAlgorithm = False
#
#------------------------------------------------------------------------------------
# TESTING QFT -- BE SURE TO COMMENT ANY OF THESE FORCED INITIAL STATE VECTORS IF DOING GROVER'S ALGORITHM
#------------------------------------------------------------------------------------
# RBW 4-15-2022 TESTING the forcing of the initial stateVector for the QFT4 and QFT32 routines
# stateVector = .500*np.array([[1],[1],[1],[1]])
# stateVector = 1.00*np.array([[0],[1],[0],[0]])
# stateVector = 1.00*np.array([[1],[0],[0],[0]])

# stateVector = .707*np.array([[0],[1],[0],[1]]) # RBW 4-16-2022 - trying this in reverse order since I put the KRON arguments back to stock to meet 'IBM's qubit 0 on the top'
#stateVector = .707*np.array([[1],[0],[1],[0]]) # RBW 4-16-2022 - back to normal order. This seems to work the same as reverse order in its final-state probabilities.
#stateVector = .707*np.array([1,0,1,0]) # RBW 4-16-2022 - back to normal order. This seems to work the same as reverse order in its final-state probabilities.

# 4-16-2022 - a normalization factor of 1/sqrt(120) makes for too-big probabilities when using the 1,2,4,8 sequence. Not sure why.
#stateVector = (1/math.sqrt(120))*np.array([1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8]) # RBW 4-16-2022 - QFT32 initial stateVector of (1,2,4,8...).
#stateVector = (1/math.sqrt(600))*np.array([1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8]) # RBW 4-16-2022 - QFT32 initial stateVector of (1,2,4,8...).
#stateVector = (1/math.sqrt(120))*np.array([[1],[2],[4],[8],[1],[2],[4],[8],[1],[2],[4],[8],[1],[2],[4],[8],[1],[2],[4],[8],[1],[2],[4],[8],[1],[2],[4],[8],[1],[2],[4],[8]]) # RBW 4-16-2022 - QFT32 initial stateVector of (1,2,4,8...).
#stateVector = 0.091*np.array([1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8,1,2,4,8]) # RBW 4-16-2022 - QFT32 initial stateVector of (1,2,4,8...).

# stateVector = (1/math.sqrt(16))*np.array([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]) # RBW 4-16-2022 - QFT32 initial stateVector (period=2).
# #stateVector = (1/math.sqrt(16))*np.array([1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]) # RBW 4-16-2022 - QFT32 initial stateVector (period=8).
# stateVector = (1/math.sqrt(16))*np.array([1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]) # RBW 4-16-2022 - QFT32 initial stateVector (period=4).
# stateVector = (1/math.sqrt(16))*np.array([1,1,0,0,-1,-1,0,0,1,1,0,0,-1,-1,0,0,1,1,0,0,-1,-1,0,0,1,1,0,0,-1,-1,0,0]) # RBW 4-17-2022 - QFT32 initial stateVector (period=4). Removing the DC.
#
# print("TESTING my initial stateVector =\n",stateVector) # TESTING
#

if runGroversAlgorithm:
    Grovers(measurementShots)
#
else: # we're here because we are NOT running Grover's algorithm
    numberOfQubits = len(gates) 
    stateVector = CreateInitialStateVector(numberOfQubits)
    # The initial state vector is now 2**numberOfQubits in size with basis state 0's amplitude equal to 1.
    gatesToProcess = gates
    numberOfGateTimes = len(gatesToProcess[0])
    
    O = [''] # set this oracle to zero length since it's not used in a non-Grovers calculation
    stateVector = MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O)

    # 9-13-2024 -- THIS ROUTINE IS NO LONGER NEEDED
    ##print("\n")
    ##CalculateAndDisplayQubitsEntanglement(numberOfQubits,stateVector) # calculate and display the qubits entanglement for this (non-Grover's) algorithm
    ##print("\n")

    # RBW 9-12-2024
    print("\n")
    MyCalculateAndDisplayQubitsEntanglement(stateVector) # calculate and display the qubits entanglement for this (non-Grover's) algorithm
    print("\n")



    print ("final stateVector (not Grover's algorithm) =\n",stateVector) # TESTING
    
    print ("\nBasis-state measurements:")
    Measure(stateVector,numberOfQubits,measurementShots) # RBW 4-28-2022

    PlotStateVector(stateVector,numberOfQubits,"QC - using matrix 'gates[]'") # plot the probabilities of the final stateVector
    plt.show(block=False) # display the plot
    
############################
#  end of MAIN CODE
############################
