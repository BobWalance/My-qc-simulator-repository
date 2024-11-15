# RBW - 3-24-2022 - Multiple-control cnot gate and cz gate seems to be working.
# RBW - 3-23-2022 - Updated using the list of control qubits.
# RBW - 3-20-2022 - Adding the 'cz' gate.

#########################################
#
#  FUNCTION -- Controlled_gates_generator
#
#########################################
# This will create a modified idenity matrix large enough to cover a CNOT and
#  other controlled gates (e.g. the cz gate)
#  whose control and target qubits are in any position over an arbitrary number
#  of qubits (specified by 'numberOfQubits'.
# The matrix created will be of the identity type with modifications.

import numpy as np
import math
import cmath

def controlled_gate_generator(gateType, numberOfQubits , controlQubits , targetQubit ):
#
# NOTE that controlQubits and targetQubit are 'zero-based'
#
    N = 2**numberOfQubits
    
    
    # RBW 4-16-2022 TESTING
#     print ("\ncontrolled_gate_generator TESTING")
#     print("gateType = ",gateType)
#     print("numberOfQubits = ",numberOfQubits)
#     print("controlQubits = ",controlQubits)
#     print("targetQubit = ",targetQubit)
#     print("\n")
    
    
    
    
    #gateMatrix = np.zeros((N,N)) # create an NxN matrix stuffed full of zeros
    gateMatrix = np.zeros((N,N),dtype=np.complex_) # 4-3-2022 create an NxN matrix stuffed full of zeros and of type complex

    maxQubitsAllowed = 13 # 2**13 is largest 2x2 matrix allowed by Python

    # first, checkfor argument errors
    if numberOfQubits > maxQubitsAllowed :
        print ("ERROR - the number of qubits is larger than", maxQubitsAllowed)
#        return cnotMatrix
        return gateMatrix # 5-5-2022
    if len(controlQubits) > maxQubitsAllowed-1 :
        print ("ERROR - the number of controlQubits is larger than numberOfQubits-1")
        return gateMatrix
    if targetQubit > (maxQubitsAllowed-1) :
        print ("ERROR - the targetQubit is larger than maxQubitsAllowed-1")
        return gateMatrix
    if ( (numberOfQubits == 0) or (len(controlQubits) == 0) ) :
        print ("ERROR - one of the arguments was ZERO")
        return gateMatrix
    # done with argument error checks
    #
    if gateType == 'x':
# user requested a CNOT gate
# CNOT matrix creation:
# To understand its operation, each row of the matrix has a
#  "basis-state modifyer row address", or simply its 'address'. The size of this
#   address is equal to 'numberOfQubits'
# The modifications to a simple identity matrix is as follows:
#   Any row whose address has its 'controlBitNumber' set will be altered from
#    what that row would be in a simple identity matrix.
#   Affected rows will be modified in this way:
#      The 'targetQubit' position in its row's address will be inverted
#       and that affected row will be created with this modified address
#
# EXAMPLE for:
#  numberOfQubits = 3 (i.e., 8 rows in this modified identity matrix)
#  controlBitNumber = 2 (zero-based) (i.e., the affected rows will be 4,5,6 and 7 (zero based)
#  targetQubit = 1 (zero-based)
#   Therefore,
#    row 0-3 (addresses=0b000-0b011)
#     1 0 0 0 0 0 0 0
#     0 1 0 0 0 0 0 0
#     0 0 1 0 0 0 0 0
#     0 0 0 1 0 0 0 0
#    row 4 (address=0b100) will be that of an identity matrix row of address 0b110
#     0 0 0 0 0 0 1 0
#    row 5 (address=0b101) will be that of an identity matrix row of address 0b111
#     0 0 0 0 0 0 0 1
#    row 6 (address=0b110) will be that of an identity matrix row of address 0b100
#     0 0 0 0 1 0 0 0
#    row 7 (address=0b111) will be that of an identity matrix row of address 0b101
#     0 0 0 0 0 1 0 0
#
        controlQubitsComposite = 0
        for cQ in controlQubits:
            #print ("cQ= ",cQ) # TESTING
            controlQubitsComposite |= 1<<(cQ) # 'or-in' all the control qubit positions
        targetQubitAddress = 1 << (targetQubit)
        #print ("TESTING controlQubitsComposite = ", controlQubitsComposite) # TESTING
        #print ("TESTING targetQubitAddress = ", targetQubitAddress)
        # NOTE: controlQubitsComposite will have a '1' in every bit position for which there are control qubits
        #  For example, for a given gate time, a single control in qubit 0 will have a controlQubitsComposite = 0b1
        for rowPositionZeroBased in range(N): # looping from 0 to N-1
            #print("rowPositionZeroBased = ",rowPositionZeroBased) # TESTING 4-16-2022
            if (rowPositionZeroBased & controlQubitsComposite == controlQubitsComposite):
                #print("rowPositionZeroBased & controlQubitsComposite == controlQubitsComposite was true for rowPositionZerobased = ",rowPositionZeroBased) # TESTING
                # the address of this row has all of its control qubits (zero-based) set, so it's a modified row
                # invert the bit position of the targetQubit (zero-based) in this row's address
                gateMatrix[ [np.bitwise_xor( rowPositionZeroBased , targetQubitAddress )] , [rowPositionZeroBased] ] = 1
            else:
                # this row is a simple identity-matrix type of row
                gateMatrix[ [rowPositionZeroBased] , [rowPositionZeroBased] ] = 1
        # all rows have been processed
        #print("cnot gate =",gateMatrix) # TESTING
        return gateMatrix # return the CNOT matrix

    elif gateType == 'z':
# user requested a cz (controlled z) gate
# If a row address has all of its control qubits and its target qubit set, the identity matrix will have a '-1' value rather than the usual '1' value in that row.      
        controlAndTargetQubitsComposite = 0
        for cQ in controlQubits:
            controlAndTargetQubitsComposite |= 1<<(cQ) # 'or-in' all the control qubit positions
        controlAndTargetQubitsComposite |= 1 << (targetQubit) # finally, 'or-in' the target qubit position
        
        for rowPositionZeroBased in range(N): # looping from 0 to N-1
            if(rowPositionZeroBased & controlAndTargetQubitsComposite == controlAndTargetQubitsComposite):
                gateMatrix[ [rowPositionZeroBased] , [rowPositionZeroBased] ] = -1
            else:
                gateMatrix[ [rowPositionZeroBased] , [rowPositionZeroBased] ] = 1
        #print("cz gate =",gateMatrix)
        # all rows have been processed
        return gateMatrix # return the cz matrix
    elif (gateType[0:1] == "p") & (len(gateType) > 1):
# user requested a cpx (controlled user-defined) phase gate
        controlAndTargetQubitsComposite = 0
        for cQ in controlQubits:
            controlAndTargetQubitsComposite |= 1<<(cQ) # 'or-in' all the control qubit positions
        controlAndTargetQubitsComposite |= 1 << (targetQubit) # finally, 'or-in' the target qubit position
        
        for rowPositionZeroBased in range(N): # looping from 0 to N-1
            if(rowPositionZeroBased & controlAndTargetQubitsComposite == controlAndTargetQubitsComposite):
                
                phasePiDivisor = int(str(gateType[1:len(gateType)]))
                #print ("phasePiDivisor for the cpx gate = ",phasePiDivisor) # TESTING
                phase = cmath.exp(1j * math.pi/phasePiDivisor)
                #print ("phase for the cpx gate = \n",phase) # TESTING                
                gateMatrix[ [rowPositionZeroBased] , [rowPositionZeroBased] ] = phase
            else:
                gateMatrix[ [rowPositionZeroBased] , [rowPositionZeroBased] ] = 1
        #print("cpx gate =",gateMatrix) # TESTING
        # all rows have been processed
        return gateMatrix # return the cpx matrix
    
    else:
        return None