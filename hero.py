import random


class hero:

	roles = ["Roaming","Farming","Support"]

	def __init__(self, name):
		self.name = name
		self.role = random.choice(self.roles)
		
	def printHero(self):
		print("Name: " + self.name + " Role: " + self.role)