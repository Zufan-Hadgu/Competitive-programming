# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * n
for i in range(1, n):
    if arr[i] < arr[i-1]:
        prefix[i] = arr[i-1] - arr[i]
    else:
        prefix[i] = 0

for i in range(1, n):
    prefix[i] += prefix[i-1]

suffix = [0] * n
for i in range(n - 2, -1, -1):
    if arr[i] < arr[i + 1]:
        suffix[i] = arr[i + 1] - arr[i]
    else:
        suffix[i] = 0

for i in range(n - 2, -1, -1):
    suffix[i] += suffix[i + 1]

for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    damage = 0

    if l < r:
        damage = prefix[r] - (prefix[l] if l > 0 else 0)
    else:
        damage = suffix[r] - (suffix[l] if r < n - 1 else 0)
    
    print(damage)
