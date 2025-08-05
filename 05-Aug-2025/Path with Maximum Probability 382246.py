# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

from collections import defaultdict
from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (v, u), prob in zip(edges, succProb):
            graph[v].append((u, prob))
            graph[u].append((v, prob))

       
        heap = [(-1.0, start_node)]
        visited = [0.0] * n
        visited[start_node] = 1.0

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob 

            if node == end_node:
                return curr_prob

            for neigh, edge_prob in graph[node]:
                path_prob = curr_prob * edge_prob
                if path_prob > visited[neigh]:
                    visited[neigh] = path_prob
                    heapq.heappush(heap, (-path_prob, neigh))

        return 0.0