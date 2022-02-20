""" Next Prime Number - by Avinash Doddi """

import math  # to use sqrt() function

def isprime(n):
	if (n == 2): return True
	if (n%2 == 0): return False
	else:
		for i in range(3, int(math.sqrt(n))+1, 2):
			if (n % i == 0): return False
		return True
		
def nextPrime(n):
	n += 1
	while True:
		if (isprime(n)): break
		else:
			prime += 1

if __name__ == '__main__':
	prime = 2
	while True:
		response = input("Enter 'y' to get next Prime Number and 'n' to exit:")
		if (response == 'y'):
			print(prime)
			prime = nextPrime(prime)
		else:
			break
		
	
	
