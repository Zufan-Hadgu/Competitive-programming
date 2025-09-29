# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if (i, j) == (m - 1, n - 1):
                return 1
            if (i, j) not in memo:
                memo[(i, j)] = dp(i, j + 1) + dp(i + 1, j)
            return memo[(i, j)]

        return dp(0, 0)
