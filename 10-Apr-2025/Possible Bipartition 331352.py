# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        gray = 0
        white = 1
        black = 2
        adj_list = defaultdict(list)
        for a,b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)

        color = {people: gray for people in range(1,n+1)}
        is_possible = True
        def dfs(node,gcolor):
            nonlocal is_possible
            if not is_possible:
                return 
            color[node] = gcolor

            for nigh in adj_list[node]:
                if color[nigh] == 0:
                    dfs(nigh,black if gcolor == white else white)
                elif color[nigh] == gcolor:
                    is_possible = False
                    return
        for people in range(1,n+1):
            if color[people] == 0:
                dfs(people,white)
        return is_possible
        