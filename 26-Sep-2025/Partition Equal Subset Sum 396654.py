# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo = {}
        def Partition(index,target):
            if index >= len(nums):
                return target == 0
            state = (index,target)
            if state not in memo:
                memo[state] = Partition(index + 1,target - nums[index]) or Partition(index+1, target)
            return memo[state]
        target = sum(nums)//2
        return  False if sum(nums) % 2 != 0 else Partition(0,target)
            
        