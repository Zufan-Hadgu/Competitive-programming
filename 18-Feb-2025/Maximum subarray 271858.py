# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         
        result = nums[0]
        maxend = nums[0]
        for i in range(1,len(nums)):
            maxend += nums[i]
            maxend = max(maxend,nums[i])
            result = max(maxend,result)
        return result
       



        

        