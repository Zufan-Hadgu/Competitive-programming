# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

 from collections import defaultdict
t = int(input())
for _ in range(t):
    matrix = []
    n, m=map(int,input().split())
    for i in range(n):
        k = list(map(int,input().split()))
        matrix.append(k)

    main = defaultdict(int)
    sec = defaultdict(int)
    for i in range(n):
        for j in range(m):
            pattern1 = i - j
            pattern2 = i + j
            main[pattern1] += matrix[i][j]
            sec[pattern2] += matrix[i][j]
    sum_over = 0
    for i in range(n):
        for j in range(m):
           winner = main[i-j] + sec[j+i] - matrix[i][j]
           sum_over = max(winner,sum_over)
    print(sum_over)
 
             
             







 
