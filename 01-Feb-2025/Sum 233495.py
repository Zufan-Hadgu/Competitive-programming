# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())
for i in range(t):
    n  = list(map(int,input().split()))
    n.sort()
    if n[-1] == n[0] + n[1]:
        print("YES")
    else:
        print("NO")
    
   

     