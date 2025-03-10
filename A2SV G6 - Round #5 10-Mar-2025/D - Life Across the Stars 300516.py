# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

def sort_item(item):
    return item[0]  

n = int(input())
bd_dict = defaultdict(int)  

for _ in range(n):
    b, d = map(int, input().split())
    bd_dict[b] += 1  
    bd_dict[d] -= 1  

sorted_dict = sorted(bd_dict.items(), key=sort_item)
 

summation = 0
result = []
for key,value in sorted_dict:
    summation += value
    result.append((key,summation))
 

people = 0
year = 0
for i in range(len(result)):
    if people < result[i][1]:
        people = result[i][1]
        year = result[i][0]

print(year,people)




 
