# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxnum = nums[0]
        res = nums[0]
        minnum = nums[0]
        res_min = nums[0]

        for i in range(1,len(nums)):  
            maxnum = max(maxnum + nums[i],nums[i])
            res = max(res,maxnum)
         
        for i in range(1,len(nums)):
            minnum = min(minnum + nums[i],nums[i])
            
            res_min = min(res_min,minnum)
        # print(res_min)
        
        return max(abs(res_min),res)
    


        


        

        
        


        