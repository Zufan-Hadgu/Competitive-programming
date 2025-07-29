# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0

        for num in nums:
            if num <= 0:
                continue
            if num == prev:
                continue  # Skip duplicates
            if num != prev + 1:
                return prev + 1
            prev = num

        return prev + 1