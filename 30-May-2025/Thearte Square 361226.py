# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

from math import ceil


n,m,a = map(int,input().split())
length = ceil(n/a)
height = ceil(m/a)

print(length*height)