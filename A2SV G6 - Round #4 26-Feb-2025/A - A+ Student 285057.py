# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

from collections import Counter


t = int(input())
for _ in range(t):
    score = list(map(int,input().split()))
    maxi = max(score)
    mini = min(score)

    maxi_d = Counter(score)

    


    
    new_score = [0]*len(score)
    for i in range(len(score)):
        if maxi == mini:
            new_score[i] = 1

    for i in range(len(score)):  
     
        if maxi - score[i] != 0:
            new_score[i] = maxi - score[i] + 1
            
        elif maxi - score[i] == 0 and maxi_d[maxi]== 1:
            new_score[i] = 0
            
        elif maxi - score[i] == 0 and maxi_d[maxi]== 2:
            new_score[i] = 1
        
    

    print(*new_score)


    

