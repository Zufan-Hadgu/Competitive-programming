# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter

t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())   
    arr = list(map(int, input().split()))   

    l = 0   
    window = Counter() 
    output = float('inf')   

    for r in range(n):   
        window[arr[r]] += 1  
        
        
        if r - l + 1 > d:
            window[arr[l]] -= 1
            if window[arr[l]] == 0:
                del window[arr[l]]   
            l += 1   
         
        if r - l + 1 == d:
            output = min(output, len(window))  

    print(output)  