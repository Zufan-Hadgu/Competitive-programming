# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0  # Start with 0 for XOR identity
        d = Counter(nums)
        for num in d:
            if d[num] != 3:
                return num
        
       
       

            
        