# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_graph = defaultdict(list)
        n = len(adj_graph)
        for u,v in edges:
            adj_graph[u].append(v)
            adj_graph[v].append(u)
        n = len(adj_graph)
        for node in adj_graph:
            if len(adj_graph[node]) == n - 1:
                return(node)
      

        