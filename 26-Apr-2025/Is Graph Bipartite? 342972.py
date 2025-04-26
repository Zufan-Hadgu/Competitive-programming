# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        gray = 0
        white = 1
        black = 2

        color = {people: gray for people in range(len(graph))}
        is_possible = True
        def dfs(node,gcolor):
            nonlocal is_possible
            if not is_possible:
                return 
            color[node] = gcolor

            for nigh in graph[node]:
                if color[nigh] == 0:
                    dfs(nigh,black if gcolor == white else white)
                elif color[nigh] == gcolor:
                    is_possible = False
                    return
        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i,white)
        return is_possible
        