# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d = defaultdict(int)
    values = defaultdict(int)

    for num in a:
        d[num] += 1
        current_count = d[num]
        values[current_count] += 1

    max_appearance = 0

    for key, val in values.items():
        max_appearance = max(key * val, max_appearance)

    print(n - max_appearance)
