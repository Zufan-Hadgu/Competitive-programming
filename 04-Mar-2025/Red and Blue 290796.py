# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))  
    m = int(input())
    b = list(map(int, input().split()))  

    
    maxr, curr_sum_r = 0, 0
    for num in r:
        curr_sum_r += num
        maxr = max(maxr, curr_sum_r)

     
    maxb, curr_sum_b = 0, 0
    for num in b:
        curr_sum_b += num
        maxb = max(maxb, curr_sum_b)

 
    print(maxr + maxb)
