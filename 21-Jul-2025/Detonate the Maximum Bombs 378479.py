# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def in_range(i, j):
            dx = bombs[i][0] - bombs[j][0]
            dy = bombs[i][1] - bombs[j][1]
            return dx * dx + dy * dy <= bombs[i][2] * bombs[i][2]

        def dfs(i, visited):
            visited.add(i)
            for j in range(len(bombs)):
                if j not in visited and in_range(i, j):
                    dfs(j, visited)

        max_count = 0
        for i in range(len(bombs)):
            visited = set()
            dfs(i, visited)
            max_count = max(max_count, len(visited))

        return max_count