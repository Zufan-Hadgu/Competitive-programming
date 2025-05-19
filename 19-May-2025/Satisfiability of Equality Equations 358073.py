# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        def find(x):
            while parent[x] != x:
                x = find(parent[x])
            return parent[x]
        def union(a,b):
            ua = find(a)
            ub  = find(b)
            parent[ua] = ub
        for equation in equations:
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            if equation[1] == '=': 
                union(a,b)
        for equation in equations:
            if equation[1] == '!':
                a = ord(equation[0]) - ord('a')
                b = ord(equation[3]) - ord('a')
                pa = find(a)
                pb = find(b)
                if pa == pb:
                    return False
        return True



        