# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n:
    print(0)

else:
    i = len(a) - 1
    minicost = 0
    diff = []

    while i >= 1:
        diff.append(a[i] - a[i - 1])
        i -= 1

    diff.sort()
    

    while k > 1:
        diff.pop()
        k -= 1

  

    minicost = sum(diff)
    print(minicost)
