""" Coin Flips - by Avinash Doddi """

import random # to use random() fuction

def randomflips():
	rand = random.random() # generates a random value
	if (rand > 0.4): return True 
	else: return False
	
def flips(n):
	heads = 0
	tails = 0
	for i in range(n):
		if (randomflips()):
			tails += 1;
		else:
			heads += 1
	print("tails:" + str(tails) + " heads:" + str(heads))	
	

if __name__ == '__main__':
	n = int(input("Enter number of flips:"))
	flips(n)
