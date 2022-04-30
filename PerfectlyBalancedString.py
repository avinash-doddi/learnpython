from collections import defaultdict
for _ in range(int(input())):
    s = input(); l = len(s)
    flag = 0
    for i in range(l-1):
        if (s[i] == s[i+1]):
            flag += 1;
    if (flag == l-1): print("YES")
    elif (flag):
        print("NO")
    else:
        if (l <= 2): print("YES")
        else: 
            d = defaultdict(int); flag = 0
            for i in range(l):
                d[s[i]] = 0;
            ref = s[0]
            for i in range(l):
                ref = d[s[0]]
                d[s[i]] += 1; j = 0;
                for x in d.values():
                    if (ref < x and j != 0): 
                        flag += 1;
                    j  += 1;
                if (flag): break
            if (flag): print("NO")
            else: print("YES")
