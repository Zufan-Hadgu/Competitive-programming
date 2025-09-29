# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def unique(right, down):
            if right >= m or down >= n:
                return 0
            if (right, down) == (m - 1, n - 1):
                return 1
            if (right, down) in memo:
                return memo[(right, down)]
            memo[(right, down)] = unique(right + 1, down) + unique(right, down + 1)
            return memo[(right, down)]

        return unique(0, 0)
