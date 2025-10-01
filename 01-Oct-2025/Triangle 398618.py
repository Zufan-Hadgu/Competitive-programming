# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        memo = {}
        def dp(i,j):
            if j > i:
                return float("inf")
            if i == n -1:
                return triangle[i][j]
            state =(i,j)
            if state not in memo:
                memo[state] = triangle[i][j] + min(dp(i+1,j) ,dp(i+1,j+1))
            return memo[state]
        return dp(0,0)
            
        