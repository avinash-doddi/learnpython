    for _ in range(int(input())):
        s = input()
        l = len(s)
        val = 96
        if (l == 1): print("Bob", ord(s) - val)
        elif (l & 1):
            sum1 = 0; sum2 = 0
            if (s[0] > s[l-1]):
                for i in range(l-1):
                    sum1 += (ord(s[i]) - val)
                sum2 = (ord(s[l-1]) - val)
                if (sum1 > sum2): print("Alice", abs(sum1 - sum2))
                else: print("Bob", abs(sum1 - sum2))
            else:
                for i in range(1,l):
                    sum1 += (ord(s[i]) - val)
                sum2 = (ord(s[0]) - val)
                if (sum1 > sum2): print("Alice", abs(sum1 - sum2))
                else: print("Bob", abs(sum1 - sum2))
        else:
            summ = 0;
            for i in s:
                summ += (ord(i) - val)
            print("Alice", summ)
