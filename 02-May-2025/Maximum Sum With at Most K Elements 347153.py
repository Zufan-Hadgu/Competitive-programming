# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heapdict = {}

        for i in range(len(grid)):
            min_heap = []
            for j in range(len(grid[0])):
                val = grid[i][j]
                if len(min_heap) < limits[i]:
                    heapq.heappush(min_heap, val)
                else:
                    if min_heap and val > min_heap[0]:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, val)
            heapdict[i] = min_heap
        ans_list = []

        for i in range(len(heapdict)):
            ans_list.extend(heapdict[i])

        output = sorted(ans_list,reverse = True)
        return sum(output[:min(k, len(output))])


        