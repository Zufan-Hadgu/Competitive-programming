# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, '032b')  
        reversed_binary = binary[::-1]  
        return int(reversed_binary, 2) 

      