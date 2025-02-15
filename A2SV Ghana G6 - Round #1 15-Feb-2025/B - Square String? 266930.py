# Problem: B - Square String? - https://codeforces.com/gym/585132/problem/B

n = int(input())
for i in range(n):
    new_str = input()
 
    len_str = len(new_str)
    first_dig = new_str[0:len_str//2]
    second_dig = new_str[len_str//2:len_str]
 
    if first_dig == second_dig:
        print('YES')
    else:
        print('NO')
            
         
       
