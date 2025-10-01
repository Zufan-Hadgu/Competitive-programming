# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}

        def dp(i,j):
            if i >= n or j < 0 or j >= n:
                return float("inf")
            
            if i == n-1:
                return matrix[i][j]  
            state = (i,j)
            if state not in memo:
                memo[state] =  matrix[i][j] + min(dp(i+1,j-1),dp(i+1,j),dp(i+1,j+1))
            return memo[state]

        return min(dp(0,j) for j in range(n))
        