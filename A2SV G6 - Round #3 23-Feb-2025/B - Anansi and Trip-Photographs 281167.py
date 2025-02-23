# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()

    back_f = []
    front = arr[:n]
    back = arr[n:]
    l = 0
    r = 0

    possible = True

    while r < len(back) and l < len(front):
        if back[r] - front[l] < x:
            possible = False
            print('NO')    
            break
        l += 1
        r += 1
    if possible:
        print('YES')





    
 
           
           
     
       


         

