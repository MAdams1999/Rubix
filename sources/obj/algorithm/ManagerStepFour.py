import sys
from sources.obj.Kubik import *
from sources.checkBackState import *
from sources.obj.managers.MixManager import *
from sources.appendListInList import appendListInList

class ManagerStepFour:
	def 	run(self, cubCurrent, solveMoveList):
		mixManager = MixManager()
		moveList = ["F", "L", "D", "L'", "D'", "F'"]
		one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 4):
			return True
		if (one == 1):
			mixManager.mixRun(moveList, cubCurrent)
			appendListInList(solveMoveList, moveList)
		
		one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 2 and two == 0):
			mixManager.mixRun(moveList, cubCurrent)
			appendListInList(solveMoveList, moveList)
		elif (one == 2 and two == 1):
			mixManager.mixRun(["D'", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D'", "F", "L", "D", "L'", "D'", "F'"])
		elif (one == 2 and two == 2):
			mixManager.mixRun(["D'", "D'", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D'", "D'", "F", "L", "D", "L'", "D'", "F'"])
		elif (one == 2 and two == 3):
			mixManager.mixRun(["D", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D", "F", "L", "D", "L'", "D'", "F'"])
		one,two = checkBackState(cubCurrent.down, "yellow")		
		
		if (one == 3 and two == 0):
			mixManager.mixRun(moveList, cubCurrent)
			appendListInList(solveMoveList, moveList)
		elif (one == 3 and two == 1):
			mixManager.mixRun(["D", "F", "L", "D", "L'", "D'", "F'"], cubCurrent)
			appendListInList(solveMoveList, ["D", "F", "L", "D", "L'", "D'", "F'"])
		
		one,two = checkBackState(cubCurrent.down, "yellow")
		if (one == 4):
			return True