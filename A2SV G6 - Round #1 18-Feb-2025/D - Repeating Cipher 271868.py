# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
enc = input()
if n == len(enc):
    x = 0
    s = []
    i = 0
    while i < n and x < n:    
        s.append(enc[x])
        i += 1
        x = x + i 
    print("".join(s))
     

   
