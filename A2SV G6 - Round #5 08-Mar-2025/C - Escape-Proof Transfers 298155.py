# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C


n, t, c = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 0
possible = 0

while r < n:
    if a[r] <= t:
        if r - l + 1 == c:
            possible += 1
            l += 1
            r += 1
        else:
            r += 1
    else:
        l = r + 1
        r += 1

print(possible)

     
    
            
    