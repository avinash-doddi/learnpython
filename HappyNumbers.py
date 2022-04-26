# for reference of problem : https://github.com/avinash-doddi/Projects-Solutions
"""Happy Number by Avinash Doddi"""
for _ in range(int(input())):
    n = input("Enter a number: ") # taking input
    sumval = 0
    while(True):
      while(n > 0):
        sumval += (n % 10) ** 2;
        n //= 10;
        
      n = sumval;
      if (n > 10): break;  # breaks since n will not become 1 no matter how many loops it takes.
  if (n == 1): print("YES")
  else: print("NO")
