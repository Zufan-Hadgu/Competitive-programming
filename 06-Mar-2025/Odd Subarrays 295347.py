# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))


    p_new = sorted(p)
    if  p == p_new:
        print(0)
        continue

    count = 0
    i = 0 
    while i < n:
        j = i + 1
        if j < n and p[i] > p[j]:
            count += 1
            i = j + 1
        else:
            i += 1
         
    print(count)
      