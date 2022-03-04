"""Check if Count Vowels by avinash-doddi"""

s = input()
vowels = ['A','a','E','e','I','i','O','o','U','u'] # list containing vowels
count = {} 
for i in s:
    if i in vowels:
        count[i] = 0
for i in s:
    if i in vowels:
        count[i] += 1
    
''' To print all the occurances'''
for x, y in count.items():
    print(str(x) + " : " + str(y))    # to get output as vowel : count
