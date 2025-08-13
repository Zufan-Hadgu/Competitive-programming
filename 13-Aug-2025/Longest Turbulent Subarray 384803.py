# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def compare(a, b):
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

        n = len(arr)
        if n < 2:
            return n

        max_len = 1
        i = 0

        for j in range(1, n):
            cmp = compare(arr[j - 1], arr[j])
            if cmp == 0:
                i = j
            elif j == n - 1 or cmp * compare(arr[j], arr[j + 1]) != -1:
                max_len = max(max_len, j - i + 1)
                i = j

        return max_len