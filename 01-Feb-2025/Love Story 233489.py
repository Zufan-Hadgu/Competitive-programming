# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
original = 'codeforces'

for i in range(t):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == original[i]:
            continue
        else:
            count += 1
                
    print(count)

  

