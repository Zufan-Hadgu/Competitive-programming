# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo = {}

        # def dp(index, prev):
        #     if index >= len(nums):
        #         return 0 

        #     state = (index, prev)
        #     if state not in memo:
        #         pick, no_pick = 0, 0
        #         if nums[index] > prev:
        #             pick = 1 + dp(index + 1, nums[index]) 
        #         no_pick = dp(index + 1, prev)
        #         memo[state] = max(pick, no_pick)
        #     return memo[state]

        # return dp(0, float('-inf'))

        memo = [1 for _ in range(len(nums))]
        def dp(index):
            if memo[index] == 1:
                for i in range(index + 1, len(nums)):
                    if nums[i] >nums[index]:
                        memo[index] = max(dp(i) + 1,memo[index])
            return memo[index]
        max_length = 0
        for i in range(len(nums)):
            max_length = max(max_length,dp(i))
        return max_length