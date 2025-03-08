# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from collections import Counter


t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    new_a = []
    output = [0] * len(b)

    for i in range(len(a)):
        new_a.append((a[i],i))


    new_a.sort()
    b.sort()

    for i in range(n):
        _,idx = new_a[i] 
        output[idx] = b[i]

    print(*output)


     