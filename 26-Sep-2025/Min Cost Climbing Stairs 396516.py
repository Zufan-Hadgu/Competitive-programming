# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def minCost(index):
            if index >= len(cost):
                return 0
    
            if index not in memo:
                memo[index] = min(
                    cost[index] + minCost(index + 2), cost[index] + minCost(index + 1)
                     
                    )
            return memo[index]
        minCost(0)
        return min(memo[0],memo[1])
        