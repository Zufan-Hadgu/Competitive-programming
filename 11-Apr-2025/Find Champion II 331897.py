# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        defeated = set()
        for u,v in edges:
            defeated.add(v)
        team = set(range(n))
        winner = team - defeated

        if len(winner) > 1:
            return -1
        return winner.pop()



        