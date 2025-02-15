# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    maximum = 0   
    right = Counter(s)   
    left = defaultdict(int)   

    for i in range(n - 1):   
        left[s[i]] += 1
        right[s[i]] -= 1
         
        if right[s[i]] == 0:
            del right[s[i]]

        f_a = len(left)   
        f_b = len(right)  
        maximum = max(maximum, f_a + f_b)  #  

    print(maximum)
