# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
first = 0
output = []

for i in range(m):
    while first < n and arr1[first] < arr2[i]:
        first += 1

    output.append(first)
 
        
print(*output)

