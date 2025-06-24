# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ans = n
    for x in range(1, n + 1):
        if x * (n - x) <= k:
            ans = min(ans, x)
    print(ans)
