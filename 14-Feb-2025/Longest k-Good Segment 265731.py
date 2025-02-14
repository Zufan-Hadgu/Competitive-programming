# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict


n,m = map(int,input().split())
arr = list(map(int,input().split()))

l = 0
d = defaultdict(int)
ans = [1,1]
for r in range(n):
    d[arr[r]] += 1

    while len(d) > m:

        d[arr[l]] -= 1
        if d[arr[l]] == 0:
            del d[arr[l]]
          
        l += 1
    if r - l > ans[1] -ans[0]:
        ans = [l + 1,r + 1]

print(*ans)

