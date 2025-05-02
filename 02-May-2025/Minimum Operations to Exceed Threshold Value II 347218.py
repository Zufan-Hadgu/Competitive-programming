# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        operation = 0
        for num in nums:
            heapq.heappush(min_heap,num)
        while len(min_heap) >= 2 and min_heap[0] < k:
            a = heapq.heappop(min_heap)
            b = heapq.heappop(min_heap)
            heapq.heappush(min_heap, 2*min(a,b) + max(a,b))
            operation += 1
        return operation


 