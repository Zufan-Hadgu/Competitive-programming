# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))


sum_1 = sum(arr1)
sum_2 = sum(arr2)


if sum_1 != sum_2:
    print(-1) 
    exit()  

p1=0
p2 = 0
count = 0


for i in range(1,n):
    arr1[i] += arr1[i-1] 
for i in range(1,m):
    arr2[i] += arr2[i-1]

while p1 < n and p2 < m:
   
    if arr1[p1] == arr2[p2]:
        count += 1
        p1 += 1
        p2 += 1
    elif arr1[p1]<arr2[p2]:
        p1 += 1
    else:
        p2 += 1
print(count)



 





            
   