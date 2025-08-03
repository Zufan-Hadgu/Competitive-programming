# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graphs = defaultdict(list)
        for s, d, p in flights:
            graphs[s].append((d, p))

        # min_price = float("inf")

        # def dfs(stop, total, current):
        #     nonlocal min_price
        #     if current == dst:
        #         min_price = min(min_price, total)
        #         return
        #     if stop > k:
        #         return

        #     for neigh, price in graphs[current]:
        #         if total + price >= min_price:
        #             continue  
        #         dfs(stop + 1, total + price, neigh)

        # dfs(0, 0, src)
        # return -1 if min_price == float("inf") else min_price

        heap = [(0,src,0)]
        visited = dict()
        while heap:
            cost,city,stop = heapq.heappop(heap)
            if city == dst:
                return cost
            if (city, stop) in visited and visited[(city, stop)] <= cost:
                continue
            visited[(city, stop)] = cost

            if stop <= k:
                for neigh,price in graphs[city]:
                    heapq.heappush(heap,(cost+ price,neigh,stop + 1))

        return -1

