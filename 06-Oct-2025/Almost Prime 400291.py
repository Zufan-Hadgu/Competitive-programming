# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
almost = 0

for i in range(2, n + 1):
    factor = set()
    num = i
    d = 2
    while d * d <= num:
        while num % d == 0:
            factor.add(d)
            num //= d
        d += 1
    if num > 1:
        factor.add(num)

    if len(factor) == 2:
        almost += 1

print(almost)
