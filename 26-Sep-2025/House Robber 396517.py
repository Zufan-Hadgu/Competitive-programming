# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # outputOdd = 0
        # outputEven = 0
        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         outputEven += nums[i]
        #     else:
        #         outputOdd += nums[i]
        # return max(outputOdd,outputEven)
        memo = {}
        def robbing (index):
            if index >= len(nums):
                return 0
            if index not in memo:
                memo[index] = max(nums[index] + robbing(index + 2)
               ,robbing(index + 1) )
            return memo[index]
        robbing(0)
        return memo[0]

                
            

        


        