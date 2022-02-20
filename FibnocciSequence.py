""" Fibnocci Sequence Up to N - by Avinash Doddi """

def fibnocci(n):
	if (n == 1):
		print(1)
	else:
		seq = [1]
		while (len(seq) < n):
			if (len(seq) == 1): seq.append(1)
			else:
				seq.append(seq[-1] + seq[-2])
		print(*seq) #prints the complete list of fibnocci sequence

if __name__ == '__main__':
	fibnocci(int(input("Enter a number to get fibnocci sequence:")))
	
	
