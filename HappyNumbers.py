# for reference of problem : https://github.com/avinash-doddi/Projects-Solutions
"""Happy Number by Avinash Doddi"""
for _ in range(int(input())):
    n = input("Enter a number: ")
    sumval = 0
    while(True):
      while(n > 0):
        sumval += (n % 10) ** 2;
        n //= 10;
        
      n = sumval;
      if (n > 10): break;
  if (n == 1): print("YES")
  else: print("NO")
