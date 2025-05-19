# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

n, m = map(int, input().split())
edges = []
for _ in range(m):
    b, e, w = map(int, input().split())
    edges.append((b, e, w))
 
edges.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ua = find(a)
    ub = find(b)
    parent[ua] = ub

minWeight = 0
edgeCount = 0  

for edge in edges:
    b, e, w = edge
    pa = find(b)
    pb = find(e)
    if pa != pb:
        minWeight += w
        union(b, e)
        edgeCount += 1

    if edgeCount == n - 1:
        print(minWeight)
        break
