# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        half = len(costs)//2
        output = 0
        def sortcost(cost):
            return cost[1] - cost[0]
        costs.sort(key = sortcost)

        for i in range(half):
            output += costs[i][1]
        
        for i in range(half,2*(half)):
            output += costs[i][0]

        return output 




        

        