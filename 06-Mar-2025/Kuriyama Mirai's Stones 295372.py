# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B


n = int(input())   
v = list(map(int, input().split()))   
m = int(input())   

prefixA = [0] * n
prefixA[0] = v[0]
for i in range(1, n):
    prefixA[i] = v[i] + prefixA[i - 1]

sorted_v = sorted(v)
prefixB = [0] * n
prefixB[0] = sorted_v[0]
for i in range(1, n):
    prefixB[i] = sorted_v[i] + prefixB[i - 1]

for _ in range(m):
    query_type, l, r = map(int, input().split())  
    l -= 1  
    r -= 1  
    
    if query_type == 1:
        result = prefixA[r] - (prefixA[l - 1] if l > 0 else 0)
        print(result)
    
    elif query_type == 2:
        result = prefixB[r] - (prefixB[l - 1] if l > 0 else 0)
        print(result)
 