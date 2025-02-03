# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in nums:
                j = nums.index(y)
                if i != j:
                    return [i,j]
            




 