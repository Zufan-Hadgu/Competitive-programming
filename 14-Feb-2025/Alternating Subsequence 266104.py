# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    i = 0
    max_sum = 0
    max_val = 0
    
    while i < n:
        max_val = arr[i]
        while i + 1 < n and arr[i] * arr[i + 1] > 0:
            max_val = max(max_val,arr[i + 1])
            i += 1
        max_sum += max_val
        i += 1
    print(max_sum)
