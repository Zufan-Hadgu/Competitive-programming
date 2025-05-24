# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
new_arr = []

l = 0
r = 0
 
while r < m or l < n:
    if r == m or l < n and arr1[l] < arr2[r]:
        new_arr.append(arr1[l])
        l += 1
    # elif arr1[l] == arr2[r]:
    #     new_arr.append(arr1[l])
    #     new_arr.append(arr2[r])
    #     l += 1
    #     r += 1
    else:
        new_arr.append(arr2[r])
        r += 1
print(*new_arr)

