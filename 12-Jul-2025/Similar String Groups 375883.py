# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(s1: str, s2: str) -> bool:
            diff = [(a, b) for a, b in zip(s1, s2) if a != b]
            
            return len(diff) == 0 or (len(diff) == 2 and diff[0] == diff[1][::-1])

        def dfs(i: int):
            for j in range(len(strs)):
                if j not in visited and are_similar(strs[i], strs[j]):
                    visited.add(j)
                    dfs(j)

        visited = set()
        groups = 0
        for i in range(len(strs)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                groups += 1
        return groups