import numpy as np
import math

from qc_simple_gates import *
from qc_functions import *
# 
# 3-26-2022 - Have split the initial Hadamard application and the repeating loop for Grovers.
#   13 qubits takes about 1/2 hour on the Raspberry Pi 4.
groversInitFullDepth = [
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"],
["h"]
]
groversGatesFullDepth = [
["O","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","C","x","h"],
["-","h","x","z","x","h"]
]

def Grovers(measurementShots):
    prompt = "\nEnter the desired number of qubits to be used in Grover's algorithm (2-"+str(len(groversInitFullDepth))+" -- 6 is default)\nNOTE THAT VALUES CLOSER TO "+str(len(groversInitFullDepth))+" RESULT IN MUCH SLOWER PROCESSING : "
    userInput = input(prompt)
    if userInput == "":
        groversQubitDepth = 6 # default value if there was no user input
    elif 2 <= float(userInput) <= len(groversInitFullDepth):
        groversQubitDepth = math.floor(float(userInput))
    else:
        groversQubitDepth = 6 # default value if user value was out-of-range

    # construct new user-defined Grovers init and gates lists depths
    groversInit  = ShortenGateList(groversInitFullDepth,groversQubitDepth)
    groversGates = ShortenGateList(groversGatesFullDepth,groversQubitDepth)

    numberOfQubits = len(groversInit)
    stateVector = CreateInitialStateVector(numberOfQubits)
    # The initial state vector is now 2**numberOfQubits in size with basis state 0's amplitude equal to 1.
    
    # Display the initialized state of the qubits
    print ("\n"+ str(measurementShots) + " measurements of the " + str(numberOfQubits) + " qubits after initialization")
    measuredValues = Measure(stateVector,numberOfQubits,measurementShots)
    title = "Histogram of the measured basis states if only the initialization if performed.\n---CLOSE THIS PLOT TO CONTINUE---"
    PlotHistogram(measuredValues,numberOfQubits,measurementShots,title)

    # Create a NxN marked matrix for use as the oracle when executing Grover's algorithm
    O = i # 'i' is the one-qubit identity matrix
    for n in range(numberOfQubits-1):
        # Note that the Kronecker product argument seems reversed but this is needed to meet the IBM simulator's convention of qubit 0 on top in the entry phase.
        O = np.kron(i,O)
    # now mark a random basis state for the Grover's algorithm to find
    basisStateMarker = math.floor((np.random.random(1)[0])*2**numberOfQubits)
    O[[basisStateMarker],[basisStateMarker]] = -1 # The oracle has now been marked
    
    # Process the Hadamard initialization gate(s) and plot the stateVector probabilities after this initialization
    gatesToProcess = groversInit # Hadamard initialization for the Grover's algorithm
    numberOfGateTimes = len(gatesToProcess[0])
    stateVector = MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O)
    # NOTE - The gates list for the Grover's main loop will contain the letter 'O'. The matrix 'O' has been created here and is passed to the MainLoopProcessor function.
    
    # Display the state of the qubits after the Hadamard gates are applied to all of the qubits
    print ("\n"+ str(measurementShots) + " measurements of the " + str(numberOfQubits) + " qubits if only the Hadamard initialization is executed:")
    measuredValues = Measure(stateVector,numberOfQubits,measurementShots) # for the Grover's Hadamard initialization
    title = "Histogram of the measured basis states if only the Hadamard initialization is performed on each qubit.\n---CLOSE THIS PLOT TO CONTINUE---"
    PlotHistogram(measuredValues,numberOfQubits,measurementShots,title)

    #
    # Process the repeating 'amplify' gate(s) in Grover's algorithm and plot the stateVector probabilities for each loop
    numLoops = math.floor(np.sqrt(2**numberOfQubits)) # This is the number of times we will go through the 'amplify' loop -- referred to as 'O(sqrt(N))'
    for n in range(numLoops):
        numberOfGateTimes = len(groversGates[0])
        gatesToProcess = groversGates
        numberOfGateTimes = len(gatesToProcess[0])
        stateVector = MainLoopProcessor(gatesToProcess,numberOfQubits,numberOfGateTimes,stateVector,O)

        print ("stateVectorGrovers = ",stateVector)
        
        print ("\n"+ str(measurementShots) + " measurements of the " + str(numberOfQubits) + " qubits if this many Grover's loops are executed -- " + str(n+1) + ":")
        measuredValues = Measure(stateVector,numberOfQubits,measurementShots) # for the loops of the Grover's algorithm (except for the last one)
        title = "Histogram of the measured basis states if " + str(n+1) + " Grover's amplify loops have been executed (" + str(numLoops) + " loops maximum).\n---CLOSE THIS PLOT TO CONTINUE---"
        PlotHistogram(measuredValues,numberOfQubits,measurementShots,title)
    input("Hit ENTER to display which row was marked ...")
    print ("\nThe marked row in the Grover's oracle matrix was",basisStateMarker)
    #
    #

