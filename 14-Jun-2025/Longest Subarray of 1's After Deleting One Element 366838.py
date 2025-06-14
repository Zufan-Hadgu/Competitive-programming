# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zeros = 0
        max_length = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1   
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            max_length = max(max_length, j - i)

        return max_length
