# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
if n%2 != 0:
    print(arr[n//2])
else:
    print(arr[(n//2)-1])
 
