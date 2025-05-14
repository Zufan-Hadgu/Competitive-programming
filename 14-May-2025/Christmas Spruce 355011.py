# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict, deque


n = int(input())
d = defaultdict(list)
for  i in range(1,n):
    v = int(input())
    d[v].append(i+1)
q = deque([1])
flag = True

while q:
    node = q.popleft()
    leaf = 0

    for child in d[node]:
        if child not in d:
            leaf += 1
        else:
            q.append(child)
    if leaf < 3:
        flag = False
        print('No')
        break
if flag:
    print('Yes')

 
         

 
    
