# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        r = 1
        output = 1
        count = 1

        while r < len(nums):
            if nums[r] == nums[r - 1]:
                r += 1
                continue
            if nums[r] == nums[r - 1] + 1:
                count += 1
                output = max(output, count)
            else:
                count = 1
            r += 1

        return output
