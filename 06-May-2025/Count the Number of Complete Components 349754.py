# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        completed = 0
 
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, nodes, edge_count):
            visited.add(node)
            nodes.append(node)
            edge_count[0] += len(graph[node])
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, nodes, edge_count)

        for node in range(n):
            if node not in visited:
                nodes = []
                edge_count = [0]
                dfs(node, nodes, edge_count)
                num_nodes = len(nodes)
                num_edges = edge_count[0] // 2   
                if num_edges == num_nodes * (num_nodes - 1) // 2:
                    completed += 1

        return completed
