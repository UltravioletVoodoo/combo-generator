from data import data

import random
import sys

def start():
	heroList = data().getHeroes()
	heroes = []

	if(len(sys.argv) == 2):
		if(isInt(sys.argv[1])):
			for x in range(int(sys.argv[1])):
				choice = random.choice(heroList)
				while(any(y.name == choice.name for y in heroes)):
					choice = random.choice(heroList)
				heroes.append(choice)
				
	else:
		heroes.append(random.choice(heroList))
	
	for x in range(len(heroes)):
		print("\nHERO " + str(x + 1) + ":")
		print("---------------------------")
		print(heroes[x].name + " | " + heroes[x].role)
		print("---------------------------\n")
	
	
	
def isInt(n):
	try:
		int(n)
		return True
	except ValueError:
		return False
		
		
start()