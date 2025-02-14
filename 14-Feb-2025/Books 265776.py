# Problem: Books - https://codeforces.com/contest/279/problem/B

n,m = map(int,input().split())
arr = list(map(int,input().split()))

count = float('-inf')
l = 0
Sum = 0

for r in range (n):
    Sum += arr[r]    
    while Sum > m:
        Sum -= arr[l]
        l += 1
    count = max(count,r-l + 1)
print(count)
    
    



