# RBW - 10-23-2024 - Fixed a bug in MyCalculateAndDisplayQubitsEntanglement(). If an under-test algorithm had only one qubit then it was causing an issue.
# RBW - 10-7-2024 - Minor improvements for MyCalculateAndDisplayQubitsEntanglement().
# RBW - 9-13-2024 - Created MyCalculateAndDisplayQubitsEntanglement() so that ptrace_outer() is not needed.

# RBW - 6-21-2022 - Implemented ptrace_outer locally in qc_functions.py rather than depending on from partial_trace_from_statevector import ptrace_outer

import numpy as np
import math
import cmath # 4-3-2022
import matplotlib.pyplot as plt
from itertools import chain

from qc_simple_gates import *
from qc_controlled_gates import controlled_gate_generator

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
        # We are here because this gate time does not contain any control qubits
        # Must now create a zero'd np.array to return
        #  to indicate to calling routine that a controlled gate
        #  was NOT found in this particular gate time
        mt = np.array([0])
        return mt # no control gates detected, so this is not a controlled-gate gate time
    #    
    # Here because this pate time DOES contain at least one controlled gate
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
        if (gateType[0:1] == "p") & (len(gateType) > 1):
            # 'px' type of target gate was found
            cpxMatrix = controlled_gate_generator(gateType, numQubits , controlQubits , qubitNumber) # 4-3-2022 gateType is a 'px' gate (e.g., 'p4')
            return cpxMatrix

    return None
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


#################################################################################################################
# 9-13-2024 -- THIS ROUTINE IS NO LONGER NEEDED
# 6-21-2022 -- 'ptrace_outer' was added from:
# https://scicomp.stackexchange.com/questions/30052/calculate-partial-trace-of-an-outer-product-in-python
# in order to get rid of any qutip dependencies
#
def ptrace_outer(u, keep, dims, optimize=False):
    """Calculate the partial trace of an outer product

    ρ_a = Tr_b(|u><u|)

    Parameters
    ----------
    u : array
        Vector to use for outer product
    keep : array
        An array of indices of the spaces to keep after
        being traced. For instance, if the space is
        A x B x C x D and we want to trace out B and D,
        keep = [0,2]
    dims : array
        An array of the dimensions of each space.
        For instance, if the space is A x B x C x D,
        dims = [dim_A, dim_B, dim_C, dim_D]

    Returns
    -------
    ρ_a : 2D array
        Traced matrix
    """
    keep = np.asarray(keep)
    dims = np.asarray(dims)
    Ndim = dims.size
    Nkeep = np.prod(dims[keep])

    idx1 = [i for i in range(Ndim)]
    idx2 = [Ndim+i if i in keep else i for i in range(Ndim)]
    u = u.reshape(dims)
    rho_a = np.einsum(u, idx1, u.conj(), idx2, optimize=optimize)
    return rho_a.reshape(Nkeep, Nkeep)


# 9-13-2024 -- THIS ROUTINE IS NO LONGER NEEDED
def CalculateAndDisplayQubitsEntanglement(numberOfQubits,stateVector):
    for val in range(0,numberOfQubits):
        # NOTE that the qubit order is reversed (from mine) in the ptrace_outer routine.
        # That is, my 0th qubit is ptrace_outer's highest-numbered qubit
        pt = ptrace_outer(stateVector,[(numberOfQubits-1)-val],[2]*numberOfQubits) # feed this routine the stateVector

        # take the trace of the square of the partial trace, then round it
        entanglementValue = round(np.trace(np.dot(pt,pt)),2) # round to two decimal places
        
        print("entanglementValue for qubit",val," = ",entanglementValue.real," [1.0 = no entanglement : 0.5 = maximum entanglement]")

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
#################################################################################################################



# RBW 10-23-2024
def MyCalculateAndDisplayQubitsEntanglement(stateVector):

    DEBUG_QE = 0 # Set this to 1 for all of the debug print statements to execute. Set to 0 for no debug printing.

    # This function implements the Reduced Density Matrix formula found in the Wikipedia article:
    # pA = summation(j -> NB)[ (IA kron <j|B) (|psi><psi|) (IA kron |j>B) ]
    #    where "kron" is the Kronecker product (aka "the tensor product")


    numberOfQubits = int(np.log2(len(stateVector)))


###    print("NUMBER OF QUBITS =",numberOfQubits)

    identityMatrix = np.array ([[1,0],[0,1]]) # create the one qubit identity matrix

    qbZeroRow = np.array([1,0]) # create a ZERO one qubit state ROW vector
    qbOneRow = np.array([0,1]) # create a ONE one qubit state ROW vector
    qbZeroCol = np.array([[1],[0]]) # create a ZERO one qubit state COLUMN vector
    qbOneCol = np.array([[0],[1]]) # create a ONE one qubit state COLUMN vector


    # Implementation of (|psi><psi|) (the full non-reduced density matrix):
    #  
    transposedConjugateSV = np.conj(stateVector)
    transposedConjugateSV = np.transpose(transposedConjugateSV)
    densityMatrix = np.kron(transposedConjugateSV,stateVector) # get the outer product of the state vector and its conjugated transpose
    if(DEBUG_QE):
      print("The density matrix is...") # for debug
      print(densityMatrix) # for debug


    for qubitNumber in range(0,numberOfQubits): # process each qubit for its level of entanglement in this outer loop

	# Initialize the variables that will hold the qubit-wide Kronecker (tensor) products.
        Ij_Zero_bra = 1
        Ij_One_bra = 1
        Ij_Zero_ket = 1
        Ij_One_ket = 1

        for Ij in range(0,numberOfQubits): # perform the Kronecker products in this inner loop
            # Implementation of (I kron I or <j|B) and (I kron I or |j>B):

             if (qubitNumber == Ij):
                 # It's time to tensor-in the qb/Zero/One/Row/Col vectors with the four Ij_One/Zero/bra/ket because we are processing the outer loop's current qubit now.
                 # All of the other tensor positions will have, or have had, the one-qubit identity matrix.
                 Ij_Zero_bra = np.kron(qbZeroRow,Ij_Zero_bra)
                 Ij_One_bra = np.kron(qbOneRow,Ij_One_bra)

                 Ij_Zero_ket = np.kron(qbZeroCol,Ij_Zero_ket)
                 Ij_One_ket = np.kron(qbOneCol,Ij_One_ket)
             else:
                 # Tensor-in a one-qubit identity matrix into the other Ij* positions (i.e., not for the current outer loop's qubit).
                 Ij_Zero_ket = np.kron(identityMatrix,Ij_Zero_ket)
                 Ij_One_ket = np.kron(identityMatrix,Ij_One_ket)
                 Ij_Zero_bra = np.kron(identityMatrix,Ij_Zero_bra)
                 Ij_One_bra = np.kron(identityMatrix,Ij_One_bra)

        if(DEBUG_QE):
          print("\n\n\n\n Here are the full tensor products for qb/Zero/One/Row/Col and the identity matrices")
          print("--- for qubit number",qubitNumber) # for debug
          print("The Ij_Zero_bra tensor product =\n", Ij_Zero_bra) # for debug
          print("... Ij_One_bra tensor product =\n", Ij_One_bra) # for debug
          print("... Ij_Zero_ket tensor product =\n", Ij_Zero_ket) # for debug
          print("... Ij_One_ket tensor product =\n", Ij_One_ket) # for debug


        rdmZero = np.matmul(Ij_Zero_bra,densityMatrix)
        if(DEBUG_QE):
          print("\nIj_Zero_bra * densityMatrix for qubit number",qubitNumber,"=")
          print(rdmZero)
        rdmZero = np.matmul(rdmZero,Ij_Zero_ket)
        rdmOne = np.matmul(Ij_One_bra,densityMatrix)
        if(DEBUG_QE):
          print("\nIj_One_bra * densityMatrix for qubit number",qubitNumber,"=")
          print(rdmOne)
        rdmOne = np.matmul(rdmOne,Ij_One_ket)


        if(DEBUG_QE):
          print("\nThe reduced density matrix (first summation term) for qubit number",qubitNumber,"=")
          print(rdmZero) # for debug
          print("") # for debug
          print("The reduced density matrix (second summation term) for qubit number",qubitNumber,"=") # for debug
          print(rdmOne) # for debug

        reducedDensityMatrix = rdmZero + rdmOne
        if(DEBUG_QE):
          print("\nThe summed reduced density matrix for qubit number",qubitNumber,"=\n") # for debug
          print(reducedDensityMatrix) # for debug

        # take the trace of the square of the reduced density matrix, then round it
        rdmSquared = np.matmul(reducedDensityMatrix,reducedDensityMatrix)


        if(DEBUG_QE):
          print("The square of the summed reduced density matrix for qubit number",qubitNumber,"=\n") # for debug
          print(rdmSquared) # for debug
          print("") # for debug


        if isinstance(rdmSquared, np.ndarray):
            entanglementValue = round(np.trace(rdmSquared),3) # round to three decimal places
        else:
            entanglementValue = 1 # There was only one qubit to process, so there was no array to take the trace of
        
        print("The entanglement value for qubit",qubitNumber," = ",entanglementValue.real," ((where 1.0 = no entanglement : 0.5 = maximum entanglement))")




def MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O):
#def MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector):
    # The main loop processing code:
    #
    for gateTimeIndex in range(numberOfGateTimes):
        qubitIndex = 0
        # first, check to see if this gate time contains a control gate
        vectorEvolvingMatrix = ControlledGateParser(gatesToProcess,numberOfQubits,gateTimeIndex)
        #print("vectorEvolvingMatrix (after ControlledGateParser = \n",vectorEvolvingMatrix) # TESTING
        #print("gateTimeIndex = ",gateTimeIndex) # TESTING
        if vectorEvolvingMatrix.any():
            dummy = 0 # needed to satisfy an otherwise empty 'if' condition
            # this gate time contained a controlled gate, so the vectorEvolvingMatrix for this gate time has already been calculated by the ControlledGateParser routine
        else :
            # Since the qubits in this gate time did not contain a controlled gate, create the vector-evolving matrix for this gate time
            #
            # Process the top (zeroth) qubit at this gate time index first so that an initial vectorEvolvingMatrix can be established that subsequent
            #  ones can be tensored with.
            
            # 4-3-2022
            # Must first check for the "px" gate in this top (zeroth) qubit (the user must supply the phase to this "px" gate
            pxGateString = gatesToProcess[qubitIndex][gateTimeIndex] # prepare for a possible "px" gate
            if (pxGateString[0:1] == "p") & (len(pxGateString) > 1):
                # a "px" gate has been found in the top (zeroth) qubit
                # The 'px' gate is a phase gate with user-supplied phase. Specifically, the divisor of pi will be supplied by the user.
                # For example:
                # "p2" will be e**(pi*i/2) for a phase of pi/2
                # "p4" will be e**(pi*i/4) for a phase of pi/4
                # "p-2" will be e**(-pi*i/2) for a phase of -pi/2 which is the same as 3*pi/2
                phasePiDivisor = int(str(pxGateString[1:len(pxGateString)]))
                #print ("phasePiDivisor = ",phasePiDivisor) # TESTING
                px = np.array ([[1,0],[0, cmath.exp(1j * math.pi/phasePiDivisor)]]) # phasePiDivisor must be supplied by the user
                #print ("px = \n",px) # TESTING
                vectorEvolvingMatrix = px
            else: # the zeroth qubit for this gate time was not a "px" gate
                vectorEvolvingMatrix = eval(gatesToProcess[qubitIndex][gateTimeIndex])

            # The vectorEvolvingMatrix now has the first matrix found in the top qubit for this gate time
            #          
            if (gatesToProcess[qubitIndex][gateTimeIndex] == "O"):
                # A Grover's oracle has been found. Do not tensor-in any other matrices.
                dummy = 0; # this is needed because no other work is done here
            else:
                # 4-3-2022 - need to process to possible "px" gate for qubits beyond the top (zeroth) one
                # tensor all qubits that might be beyond the zeroth qubit (for this gate time)
                for nq in range(numberOfQubits-1):
                    qubitIndex = qubitIndex + 1 # point to the next-higher qubit (the zeroth qubit has already been tensored into the matrix
                    pxGateString = gatesToProcess[qubitIndex][gateTimeIndex] # prepare for a possible "px" gate
                    if (pxGateString[0:1] == "p") & (len(pxGateString) > 1):
                        # a "px" gate has been found in this qubit
                        # The 'px' gate is a phase gate with user-supplied phase. Specifically, the divisor of pi will be supplied by the user.
                        # For example:
                        # "p2" will be e**(pi*i/2) for a phase of pi/2
                        # "p4" will be e**(pi*i/4) for a phase of pi/4
                        # "p-2" will be e**(-pi*i/2) for a phase of -pi/2 which is the same as 3*pi/2
                        phasePiDivisor = int(str(pxGateString[1:len(pxGateString)]))
                        #print ("phasePiDivisor (past the zeroth qubit) = ",phasePiDivisor) # TESTING
                        px = np.array ([[1,0],[0, cmath.exp(1j * math.pi/phasePiDivisor)]]) # phasePiDivisor must be supplied by the user
                        #print ("px (past the zeroth qubit) = \n",px) # TESTING
                        # Note that the Kronecker product argument seems reversed but this is needed to meet the IBM simulator's convention of qubit 0 on top in the entry phase.
                        vectorEvolvingMatrix = np.kron(px,vectorEvolvingMatrix) # tensor-in the "px" gate with the existing vectorEvolvingMatrix
                    else: # the qubit for this gate time was not a "px" gate
                        # Note that the Kronecker product argument seems reversed but this is needed to meet the IBM simulator's convention of qubit 0 on top.
                        vectorEvolvingMatrix = np.kron(eval(gatesToProcess[qubitIndex][gateTimeIndex]),vectorEvolvingMatrix)
                        #print("vectorEvolvingMatrix (non-controlled gate) =\n",vectorEvolvingMatrix) # TESTING
                        #print("gateTimeIndex = ",gateTimeIndex) # TESTING
                    #
        # The vector-evolving matrix was either already created by the controlled-gate parser, or it has been fully tensored together for this gate time,
        #  so now it's time to multiply this matrix into the state vector.
        stateVector = np.dot(vectorEvolvingMatrix,stateVector)
        #print ("vectorEvolvingMatrix = \n", vectorEvolvingMatrix) # TESTING
        #print ("interim stateVector =\n",stateVector) # TESTING
        #
    return stateVector


def Measure(stateVector,numberOfQubits,measurementShots):
    probabilityMagnitude = np.conj(stateVector) * stateVector # calculate the probability magnitudes for all ofthe basis states
    probabilityMagnitude = probabilityMagnitude.real # this is done to remove warning in plt.bar - matplotlib warning ("ComplexWarning: Casting complex values to real discards..."

    measuredValues = []

    for n in range(measurementShots):
        measured = np.random.choice( a=list(range(2**numberOfQubits)), p=list(chain.from_iterable(probabilityMagnitude)))
        measuredValues.append(measured) # add to the list of measured values
        print(measured, end=' ') # end=' ' adds a space to the end of the printed value rather than a CR/LF
    print("\n")
    return measuredValues


def PlotHistogram(measuredValues,numberOfQubits,measurementShots,title):   
    plt.xticks(np.arange(2**numberOfQubits)) # this done so that the 'x' ticks and labels are one per basis state, but SLOWS plotting greatly when processing more than 8 qubits
    yLabel = "number of basis states measured (" + str(measurementShots) + " total measurements)"
    plt.ylabel(yLabel)
    plt.xlabel('basis state')
    plt.suptitle(title, fontsize=20)
    plt.hist(measuredValues,bins=np.arange(2**numberOfQubits)-0.5)
    plt.show()


def CreateInitialStateVector(numberOfQubits):
    # create the first state vector to include all qubits
    stateVector = np.array([[1],[0]]) # This is the starting state vector for one qubit.
    v1 = np.array([[1],[0]])
    for nq in range(numberOfQubits-1):
        # Note that the Kronecker product argument seems reversed but this is needed to meet the IBM simulator's convention of qubit 0 on top in the entry phase.
        stateVector=np.kron(v1,stateVector) # lengthen the initial state vector with the next qubit
    return stateVector

def ShortenGateList(list,newQubitDepth):
    shortenedList = []
    for n in range(newQubitDepth-1):
        # first do all but the last qubit
        shortenedList.append(list[n])
    # finally add in the last qubit from the original list
    shortenedList.append(list[len(list)-1])
    return shortenedList