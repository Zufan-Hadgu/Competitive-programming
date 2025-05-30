# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        once = 0
        while r < len(nums) and l < len(nums):
            if nums[r] == 0:
                l = r+1
            once = max(r-l +1,once)
            r += 1
    
        return once