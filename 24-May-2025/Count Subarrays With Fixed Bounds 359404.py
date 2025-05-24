# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        ind_min = - 1
        ind_max = - 1
        ind_invalid = - 1

        for i , num in enumerate(nums):
            if num > maxK or num < minK:
                ind_invalid = i
            if num == minK:
                ind_min  = i
            if num == maxK:
                ind_max = i
            valid_region = min(ind_min,ind_max)
            ans += max(0,valid_region - ind_invalid)
        return ans
        