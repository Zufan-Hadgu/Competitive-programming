# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0] * n
        adjList = defaultdict(list)
        
        for u, v in edges:
            indegree[v] += 1
            adjList[u].append(v)
         
        q = deque([i for i in range(n) if indegree[i] == 0])
        res = [set() for _ in range(n)]
        
        while q:
            curr = q.popleft()
            for nbr in adjList[curr]:
                
                res[nbr].add(curr)
                res[nbr].update(res[curr])
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        
        return [sorted(list(ancestors)) for ancestors in res]
