# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # memo = {}

        # def dp(i,j):
        #     if i >= n or j < 0 or j >= n:
        #         return float("inf")
            
        #     if i == n-1:
        #         return matrix[i][j]  
        #     state = (i,j)
        #     if state not in memo:
        #         memo[state] =  matrix[i][j] + min(dp(i+1,j-1),dp(i+1,j),dp(i+1,j+1))
        #     return memo[state]

        # return min(dp(0,j) for j in range(n))

        #bottom up

        memo = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    memo[i][j] = matrix[i][j]
                else:
                    down = memo[i-1][j]
                    left = memo[i-1][j-1] if j-1 >= 0 else float("inf")
                    right = memo[i-1][j+1] if j+1 < n else float("inf")
                    memo[i][j] = matrix[i][j] + min(down, left, right)
        return min(memo[n-1]) 

            
        