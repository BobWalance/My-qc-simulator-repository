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
import math
import matplotlib.pyplot as plt
#
#import all of the qc modules
from qc_controlled_gates import controlled_gate_generator
from qc_simple_gates import *
from qc_algorithms import *
#
# 'qutip' is needed for the partial trace calculations used in generating the qubit entanglement values.
# qutip installation is much easier than older versions:
#  pip install qutip
from partial_trace_from_statevector import ptrace_outer
from partial_trace_from_statevector import partial_trace_orig # this version is just used for testing

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
runGroversAlgorithm = False
plotProbabilitiesForAllGroversLoops = False # this will be used to determine if the user wants each Grover's loop stateVector to be plotted




############################
# SUBROUTINES
############################
def ControlledGateParser(gatesToProcess,numQubits,gateNumber):
    # This routine will be called at the beginning of every gate time in order to check
    #  if there is a controlled gate in that gate time
    #
    # first, loop through this gate time (a particular column in the gates list) to see if there is a control or controls
    controlQubits = [] # 3-23-2022 will hold a list of the control qubits (zero-based) for a given gate time
    for qubitNumber in range(numQubits):
        gateType = gatesToProcess[qubitNumber][gateNumber]
        if gateType == 'C':
            # control gate detected
            controlQubits.append(qubitNumber) # 3-23-2022 save the control qubit numbers associtated with the found control gate
    # done searching for control gate(s)
    
    if len(controlQubits) == 0:
        # Must now create a zero'd np.array to return
        #  to indicate to calling routine that a controlled gate
        #  was NOT found in this particular gate time
        mt = np.array([0])
        return mt # no control gates detected, so this is not a controlled-gate gate time
    #    
    # Here because this pate time DOES contain a controlled gate
    # Loop through this gate time to find the type of target gate
    for qubitNumber in range(numQubits):
        gateType = gatesToProcess[qubitNumber][gateNumber]
        if gateType == 'x':
            # 'x' type of target gate was found
            # note that controlQubits list and qubitNumber are 'zero-based'
            cnotMatrix = controlled_gate_generator('x', numQubits , controlQubits , qubitNumber) # 3-23-2022 controlQubits is a list of the qubit numbers of all the controls
            return cnotMatrix
        if gateType == 'z':
            # 'z' type of target gate was found
            # note that controlQubits and qubitNumber are 'zero-based'
            czMatrix = controlled_gate_generator('z', numQubits , controlQubits , qubitNumber) # 3-23-2022 controlQubits is a list of the qubit numbers of all the controls
            return czMatrix
#
#

def PlotStateVector(stateVector,numberOfQubits,plotTitle): # plot the probabilities of the final stateVector

    probabilityMagnitude = np.conj(stateVector) * stateVector # calculate the probability magnitudes for all ofthe basis states

    probabilityMagnitude = probabilityMagnitude.real # this is done to remove warning in plt.bar - matplotlib warning ("ComplexWarning: Casting complex values to real discards..."

    plt.bar(list(range(2**numberOfQubits)),np.asarray(probabilityMagnitude.flatten())) # default width, and must convert the probabilityMagnitude to a 1D array for the plt.bar function

    plt.xticks(np.arange(2**numberOfQubits)) # this done so that the 'x' ticks and labels are one per basis state, but SLOWS plotting greatly
                                             #  when processing more than 8 qubits
    plt.yticks(np.arange( 0 , 1.1 , 0.1 )) # this done to keep the 'y' max tick always at 1

    plt.ylabel('probability')
    plt.xlabel('basis state')
    
    plt.suptitle(plotTitle, fontsize=20)
    
    plt.gcf().set_size_inches(16, 14)

def CalculateAndDisplayQubitsEntanglement(numberOfQubits,stateVector):
    for val in range(0,numberOfQubits):
        # NOTE that the qubit order is reversed (from mine) in the ptrace_outer routine.
        # That is my 0th qubit is ptrace_outer's highest-numbered qubit
        pt = ptrace_outer(stateVector,[(numberOfQubits-1)-val],[2]*numberOfQubits) # feed this routine the stateVector

        # take the trace of the square of the partial trace, then round it to one decimal place
        entanglementValue = round(np.trace(np.dot(pt,pt)),1)
        
        print("entanglementValue for qubit",val," = ",entanglementValue)

    # HOW TO USE ptrace_outer):
    # def ptrace_outer(u, keep, dims, optimize=False):
    #     """Calculate the partial trace of an outer product
    # 
    #     ρ_a = Tr_b(|u><u|)
    # 
    #     Parameters
    #     ----------
    #     u : array
    #         Vector to use for outer product
    #     keep : array
    #         An array of indices of the spaces to keep after
    #         being traced. For instance, if the space is
    #         A x B x C x D and we want to trace out B and D,
    #         keep = [0,2]
    #     dims : array
    #         An array of the dimensions of each space.
    #         For instance, if the space is A x B x C x D,
    #         dims = [dim_A, dim_B, dim_C, dim_D]
    # 
    #     Returns
    #     -------
    #     ρ_a : 2D array
    #         Traced matrix
    #     """
    #

def MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O):
    # The main loop processing code:
    #
    for gateTimeIndex in range(numberOfGateTimes):
        qubitIndex = 0
        # first, check to see if this gate time contains a control gate
        vectorEvolvingMatrix = ControlledGateParser(gatesToProcess,numberOfQubits,gateTimeIndex)
    #    print("vectorEvolvingMatrix (after ControlledGateParser = \n",vectorEvolvingMatrix) # TESTING
        if vectorEvolvingMatrix.any():
            dummy = 0 # needed to satisfy an otherwise empty 'if' condition
            # this gate time contained a controlled gate, so the matrix for this gate time is available
        else :
            # since the qubits in this gate time did not contain a controlled gate, create the vector-evolving matrix for this gate time
            # begin with the top (zeroth) qubit at this gate time index
            vectorEvolvingMatrix = eval(gatesToProcess[qubitIndex][gateTimeIndex])           
            # The vectorEvolvingMatrix now has the first matrix found in the top qubit for this gate time
            #          
            if (gatesToProcess[qubitIndex][gateTimeIndex] == "O"):
                # A Grover's oracle has been found. Do not tensor-in any other matrices.
                dummy = 0; # this is needed because no other work is done here
            else:
                # tensor all qubits that might be beyond the zeroth qubit (for this gate time)
                for nq in range(numberOfQubits-1):
                    qubitIndex = qubitIndex + 1 # point to the next-higher qubit (the zeroth qubit has already been tensored into the matrix
                    vectorEvolvingMatrix = np.kron(eval(gatesToProcess[qubitIndex][gateTimeIndex]),vectorEvolvingMatrix)           
        # The vector-evolving matrix was created by the controlled-gate parser, or it has already been fully tensored together for this gate time,
        #  so now it's time to multiply this matrix into the state vector.
        stateVector = np.dot(vectorEvolvingMatrix,stateVector)
        #print ("stateVector =\n",stateVector) # TESTING
        #
    return stateVector
############################
# end of SUBROUTINES
############################
#
#
#
####################################################################################
#                         MAIN CODE
####################################################################################
print ("Processing started...")
#
userInput = input("Do Grover's algorithm? (y then Enter for YES)")
if userInput == "y":
    runGroversAlgorithm = True
    userInput = input("Plot the state vector probabilities after each Grover's loop? (y then Enter for YES)")
    if userInput == "y":
        plotProbabilitiesForAllGroversLoops = True
#
if runGroversAlgorithm:
    numberOfQubits = len(groversInit)
else:
    numberOfQubits = len(gates)
#
# create the first state vector to include all qubits
stateVector = np.array([[1],[0]]) # This is the starting state vector for one qubit.
#
v1 = np.array([[1],[0]])
for nq in range(numberOfQubits-1):
    stateVector=np.kron(v1,stateVector) # lengthen the initial state vector with the next qubit
# The initial state vector is now 2**numberOfQubits in size with basis state 0's amplitude equal to 1.
#
if runGroversAlgorithm:
    # Create a NxN marked matrix for use as the oracle when executing Grover's algorithm
    O = i # 'i' is the one-qubit identity matrix
    for n in range(numberOfQubits-1):
        O = np.kron(i,O)
    # now mark a random basis state for the Grover's algorithm to find
    basisStateMarker = math.floor((np.random.random(1)[0])*2**numberOfQubits)
    O[[basisStateMarker],[basisStateMarker]] = -1
    print ("\nThe basis state marked in the Grover's oracle was",basisStateMarker)
    #
    # Process the Hadamard initialization gate(s) and plot the stateVector probabilities after this initialization
    gatesToProcess = groversInit # Hadamard initialization for the Grover's algorithm
    numberOfGateTimes = len(gatesToProcess[0])
    numLoops = math.floor(np.sqrt(2**numberOfQubits)) # This is the most number of times through the loop -- referred to as 'O(sqrt(N))'
    stateVector = MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O)
    print ("\nQubits entanglement after the Hadamard initialization:")
    CalculateAndDisplayQubitsEntanglement(numberOfQubits,stateVector) # calculate and display the qubits entanglement after Hadamard initialization in Grover's algorithm
    #
    if plotProbabilitiesForAllGroversLoops:
        PlotStateVector(stateVector,numberOfQubits,"After the Hadamard initialization - using matrix 'groversInit[]'") # plot the probabilities of this stateVector
        plt.show(block=False) # display the plot
        plt.pause(3) # display the plot for a short time before closing it
        print ("") # needed for the plot to appear - not sure why this is
        plt.close()
        #
    # Process the repeating gate(s) in Grover's algorithm and plot the stateVector probabilities for each loop
    for n in range(numLoops):
        numberOfGateTimes = len(groversGates[0])
        gatesToProcess = groversGates
        numberOfGateTimes = len(gatesToProcess[0])
        stateVector = MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O)
        print ("\nQubits entanglement after Grover's loop " + str(n+1) + " of " + str(numLoops) + ":")
        CalculateAndDisplayQubitsEntanglement(numberOfQubits,stateVector) # calculate and display the qubits entanglement after each Grover's loop
    #
        if plotProbabilitiesForAllGroversLoops & (n < numLoops-1):
            PlotStateVector(stateVector,numberOfQubits,"Grover's loop "+ str(n+1) + " of " + str(numLoops) + " using matrices 'groversInit[]' and 'groversGates[]'") # plot the probabilities of this stateVector
            plt.show(block=False) # display the plot
            plt.pause(3) # display the plot for a short time before closing it
            print ("") # needed for the plot to appear - not sure why this is
    #        if (n != numLoops-1):
            plt.close()
    #
    PlotStateVector(stateVector,numberOfQubits,"Grover's loop "+ str(numLoops) + " of " + str(numLoops) + " using matrices 'groversInit[]' and 'groversGates[]'") # plot the probabilities of the final stateVector of Grover's algorithm
    plt.show(block=False) # display the plot
    #
else: # we're here because we are NOT running Grover's algorithm
    gatesToProcess = gates
    numberOfGateTimes = len(gatesToProcess[0])
    O = [] # set this to zero length since it's not used in a non-Grovers calculation
    stateVector = MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O)
    CalculateAndDisplayQubitsEntanglement(numberOfQubits,stateVector) # calculate and display the qubits entanglement after each Grover's loop
    PlotStateVector(stateVector,numberOfQubits,"QC - using matrix 'gates[]'") # plot the probabilities of the final stateVector
    plt.show(block=False) # display the plot

############################
#  end of MAIN CODE
############################
