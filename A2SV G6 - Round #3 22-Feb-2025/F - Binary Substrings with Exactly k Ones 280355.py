# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict


k  = int(input())
arr = list(map(int,input().strip()))

d = defaultdict(int)
d[0] = 1
count = 0

for i in range(1,len(arr)):
    arr[i] += arr[i-1]

for num in arr:    
    count += d[num - k]
    d[num] += 1
print(count) 




