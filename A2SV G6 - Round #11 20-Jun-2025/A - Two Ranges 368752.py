# Problem: A - Two Ranges - https://codeforces.com/gym/604781/problem/A

q = int(input())
for _ in range(q):
    l1,r1,l2,r2 = list(map(int,input().split()))
    ans = []
    if l1 != l2:
        print(l1, l2)
    else:
        print(l1, l2 + 1)
 

        

