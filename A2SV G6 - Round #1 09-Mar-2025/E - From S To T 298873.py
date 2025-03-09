# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import defaultdict


q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()

    i = 0
    j = 0
    while i < len(s)  and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i != len(s):
        print("NO")
        continue
       

    count_t = defaultdict(int)
    for letter in t:
        count_t[letter] += 1
    

    count_s_p = defaultdict(int)
    for letter in s + p:
        count_s_p[letter] += 1

    for key, value in count_t.items():
        if count_s_p[key] < value:
            print('NO')
            break
    else:
        print('YES')

    


