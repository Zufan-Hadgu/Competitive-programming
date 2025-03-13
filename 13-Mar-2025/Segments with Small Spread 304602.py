# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

decr = deque()
incr = deque()
l = 0
output = 0

for r in range(n):
    while decr and decr[-1] < a[r]:
        decr.pop()
    decr.append(a[r])

    while incr and incr[-1] > a[r]:
        incr.pop()
    incr.append(a[r])

    while decr[0] - incr[0] > k:
        value = a[l]
        if decr[0] == value:
            decr.popleft()
        if incr[0] == value:
            incr.popleft()
        l += 1

    output += r - l + 1

print(output)
