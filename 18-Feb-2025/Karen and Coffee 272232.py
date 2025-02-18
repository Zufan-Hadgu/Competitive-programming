# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int,input().split())
diff = [0] * 200002
m = len(diff)

 
for _ in range(n):
    l,r = map(int,input().split())
    diff[l] += 1
    diff[r+1] -= 1
  
for i in range(1,m ):
    diff[i] += diff[i-1]
for i in range(m):
    if diff[i] >= k:
        diff[i] = 1
    else:
        diff[i] = 0
for i in range(1,m):
    diff[i] += diff[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(diff[r] - diff[l - 1])  










