# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v,score in roads:
            adj_list[u].append((v,score))
            adj_list[v].append((u,score))
        min_score = float('inf')
        visited = set()
        def dfs(node):
            nonlocal min_score
            visited.add(node)
            for neighboar, score in adj_list[node]:
                min_score = min(min_score,score)
                if neighboar not in visited:
                    dfs(neighboar)
        dfs(1)
        return min_score
        