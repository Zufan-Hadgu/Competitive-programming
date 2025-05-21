# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            px = find(x)
            py = find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
        p1 = 0
        p2 = 0
        component = defaultdict(list)
        while p1 < len(s1) and p2< len(s2):
            w1 = find(ord(s1[p1]) - ord('a'))   
            w2 = find(ord(s2[p2]) - ord('a'))
            union(w1,w2)    
            p1 += 1
            p2 += 1
        output = ""
        for s in baseStr:
            ps = find(ord(s)-ord('a'))
            output += chr(ps + ord('a'))
        return output

             





        # if parent[w1] == parent[w2]:
        #     #     if s1[p1] in component:
        #     #         component[s1[p1]].append(s2[p2])
        #     #     elif s2[p1] in component:
        #     #         component[s2[p1]].append(s1[p2])
        #     #     else:
        #     #         component[s1[p1]].append(s2[p2])  