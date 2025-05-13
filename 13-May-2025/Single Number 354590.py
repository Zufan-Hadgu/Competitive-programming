# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f_bit = 0
        for num in nums:
            f_bit = f_bit ^ num
        return f_bit
        
        