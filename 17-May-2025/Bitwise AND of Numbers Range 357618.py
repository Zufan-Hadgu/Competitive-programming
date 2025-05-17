# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask = 0xFFFFFFFF  
        while (left & mask) != (right & mask):
            mask <<= 1   
        return left & mask
