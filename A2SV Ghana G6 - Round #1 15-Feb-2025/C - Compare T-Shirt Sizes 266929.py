# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585132/problem/C

n = int(input())
for i in range(n):
    n,k = input().split()
    # print(n,k)
    len_n = len(n)
    len_k = len(k)
    
    if n == k:
        print('=')
        continue
    if n[len_n-1]=='S' and k[len_k-1] =='S':
        if len_n > len_k:
            print('<')
        elif len_n < len_k:
            print('>')
        
    elif n[len_n-1]=='L' and k[len_k-1] =='L':
        if len_n > len_k:
            print('>')
        elif len_n < len_k:
            print('<')
         
    else:
        if n[len_n-1]=='L' and k[len_k-1] =='S':
            print('>')

        elif n[len_n-1]=='S' and k[len_k-1] =='L':
            print('<')
        elif n[len_n-1] =='L' and  k[len_k-1] =='M':
            print('>')
        elif n[len_n-1] =='M' and  k[len_k-1] =='L':
            print('<')
        
        elif n[len_n-1] =='S' and  k[len_k-1] =='M':
            print('<')
        elif n[len_n-1] =='M' and  k[len_k-1] =='S':
            print('>')
        
    
 



        

