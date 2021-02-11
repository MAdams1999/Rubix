import sys
from sources.obj.algorithm.ManagerStepOne import *
from sources.obj.algorithm.ManagerStepTwo import *
from sources.obj.algorithm.ManagerStepThree import *
from sources.obj.algorithm.ManagerStepFour import *
from sources.obj.algorithm.ManagerStepFive import *
from sources.obj.algorithm.ManagerStepSix import *
from sources.obj.algorithm.ManagerStepSeven import *

from sources.obj.Kubik import *

class algorithm:
	def __init__(self, cub):
		self.cub = cub
		self.solveMoveList = list()

	def 	run(self):
		cubOrigin = Kubik(3)

		managerStepOne = ManagerStepOne(cubOrigin)
		managerStepTwo = ManagerStepTwo(cubOrigin)
		managerStepThree = ManagerStepThree(cubOrigin)
		managerStepFour = ManagerStepFour()
		managerStepFive = ManagerStepFive(cubOrigin)
		managerStepSix = ManagerStepSix(cubOrigin)
		managerStepSeven = ManagerStepSeven(cubOrigin)
		
		managerStepOne.run(self.cub, self.solveMoveList)
		managerStepTwo.run(self.cub, self.solveMoveList)
		managerStepThree.run(self.cub, self.solveMoveList)
		managerStepFour.run(self.cub, self.solveMoveList)
		managerStepFive.run(self.cub, self.solveMoveList)
		managerStepSix.run(self.cub, self.solveMoveList)
		managerStepSeven.run(self.cub, self.solveMoveList)
		return (self.solveMoveList)