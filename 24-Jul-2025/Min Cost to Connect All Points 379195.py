# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)]  
        total_cost = 0
        connected = 0

        while connected < n:
            cost, i = heapq.heappop(min_heap)
            if visited[i]:
                continue
            visited[i] = True
            total_cost += cost
            connected += 1

            for j in range(n):
                if not visited[j]:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (dist, j))

        return total_cost