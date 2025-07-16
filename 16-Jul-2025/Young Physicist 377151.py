# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

n = int(input())
sum_m = [0,0,0]
for _ in range(n):
    a,b,c = map(int,input().split())
    sum_m[0] += a
    sum_m[1] += b
    sum_m[2] += c
if sum_m[0] == 0 and sum_m[1] == 0 and sum_m[2] == 0:
    print("YES")
else:
    print("NO")

