# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = 0
max_length = 0
left = 0

for i in range(n):
    current_sum += arr[i]
     
    while current_sum > s:
        current_sum -= arr[left]
        left += 1
    
     
    max_length = max(max_length, i - left + 1)

 
print(max_length)
