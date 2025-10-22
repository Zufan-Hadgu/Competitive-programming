# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        max_len = float("-inf")
        for num in arr:
            dp[num] = dp.get(num-difference , 0) + 1
            max_len = max(max_len ,dp[num])
        return max_len


        