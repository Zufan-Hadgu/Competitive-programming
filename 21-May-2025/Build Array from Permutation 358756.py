# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for i in range(len(nums)):
            output[i] = nums[nums[i]]
        return output

        