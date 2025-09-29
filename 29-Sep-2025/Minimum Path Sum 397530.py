# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def dp(i,j):
            if i >= m or j >= n:
                return float('inf')
            if (i,j) == (m-1,n-1):
                return grid[i][j]
            state = (i,j)
            if state not in memo:
                memo[state] = grid[i][j] + min(dp(i,j+1),dp(i+1,j))
            return memo[state]
        return dp(0,0)
        