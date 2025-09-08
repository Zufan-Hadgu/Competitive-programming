# Problem: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    total = a + b
    team = total // 4
    print(min(a,b,team))