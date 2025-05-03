# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i,equ in enumerate(equations):
            x,y = equ
            graph[x].append([y,values[i]])
            graph[y].append([x,1/values[i]])


        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            q = deque([[start, 1.0]])
            visited = set([start])

            while q:
                n, v = q.popleft()
                if n == end:
                    return v
                for nei, weight in graph[n]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append([nei, v * weight])
            return -1.0


                
        ans = []
        for a,b in queries:
            
            ans.append(bfs(a,b))
   
        return ans


        