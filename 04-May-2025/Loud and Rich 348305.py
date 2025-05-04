# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

 

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * n
 
        for a, b in richer:
            graph[a].append(b)   
            indegree[b] += 1

    
        res = list(range(n))
        
        
        q = deque([i for i in range(n) if indegree[i] == 0])
        
        while q:
            person = q.popleft()
            for neighbor in graph[person]:
 
                if quiet[res[person]] < quiet[res[neighbor]]:
                    res[neighbor] = res[person]
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res
