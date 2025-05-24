# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n , m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
 
i = 0
for num in arr2:
    while i < n and  arr1[i] < num:
        i += 1
    print(i ,end =  ' ')