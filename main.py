import sys
from sources.readFile import *
from sources.errorExit import *
from sources.obj.managers.ValidationManager import ValidationManager
from sources.obj.managers.MixManager import MixManager
from sources.obj.Kubik import Kubik
from sources.obj.CheckerColors import CheckerColors
from sources.obj.algorithm.Algorithm import *
from sources.printSolution import *
from sources.optimizationMove import *

stringUsage = "Hey this is how you use me idot: main.py  [-i or -f or --help or -h] [count i or fileName] [-g or -gt or -wc]"

if (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
    print ("    Availabe moves [ F B R L U D ]")
    print ("    Modificator [ ' ] and [ 2 ]")
    print ("    Example: F2 B' U2")
    print ("    -i. This is  a random generator Mix moving.\n    Example: python main.py -f 25 -g")
    print ("    -f. This is  to read from file.\n    Example: python main.py -i fileName -g")
    print ("    -g. This is a color printing Solution.\n    Example: python main.py -i 25 -g")
    print ("    -gt. This is without color.\n    Example: python main.py -f fileName -gt")
    print ("    -wc. -wc. This is without print Solution. Only steps move\n    Example: python main.py -f fileName -wc")
    sys.exit(-1)

if (len(sys.argv) != 4 and len(sys.argv) != 2):
    errorExit(stringUsage)
if (len(sys.argv) == 4 and ((sys.argv[1] != "-f" and sys.argv[1] != "-i") or (sys.argv[3] != "-g" and sys.argv[3] != "-gt" and sys.argv[3] != "-wc"))):
    errorExit(stringUsage)

if ((len(sys.argv) == 4) and sys.argv[1] == "-f"):
    readBuffer = readFile(sys.argv[2])
    validationManager = ValidationManager(readBuffer)
    validationManager.run()
elif (len(sys.argv) == 2):
    readBuffer = sys.argv[1]
    validationManager = ValidationManager(sys.argv[1])
    validationManager.run()
mixManager = MixManager()
moveList = list()
if ((len(sys.argv) == 4) and sys.argv[1] == "-i"):
    try:
        i = int(sys.argv[2])
        if (i <= 0):
            sys.exit(-1)
        moveList = mixManager.generateRandomMove(int(sys.argv[2]))
    except:
        errorExit("Invalid digital count")
else:
    moveList = readBuffer.split(" ")
cub = Kubik(3)
mixManager.mixRun(moveList, cub)
cub.mathHash()
algorithm = algorithm(cub)
cubOrigin = Kubik(3)
if (len(sys.argv) == 4 and sys.argv[3] != "-wc"):
    print ("Mix MoveList")
    for x in moveList:
        print (x, end=" ")
    print ("")
    print ("Mix state Kubik")
    if (sys.argv[3] == "-g"):
        cub.printKubik()
    else:
        cub.printKubikText()
if (cubOrigin.hash == cub.hash):
    print ("The cube is already solved")
    sys.exit(-1)
solution = algorithm.run()
subSolution = optimizationMove(solution)
mixManager.mixRun(moveList, cubOrigin)
if (len(sys.argv) == 4 and sys.argv[3] != "-wc"):
    printSolution(cubOrigin, subSolution, sys.argv[3])
else:
    i = 0
    for x in subSolution:
        if (i != 0 and i != len(subSolution)):
            print (end=" ")
        print (x, end="")
        i += 1
    print ("")
