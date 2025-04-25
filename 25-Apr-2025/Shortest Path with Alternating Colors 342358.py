# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        output = [-1 ]*n
        print(output)

        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        
        output[0] = 0
        queue = deque([(0,0,None)])
        visited = set()

        while queue:
            node,length,color = queue.popleft()
            if output[node] == -1:
                output[node] = length

            if color != "red":
                for i in red[node]:
                    if (i,'red') not in visited:
                        visited.add((i,'red'))
                        queue.append([i,length + 1,'red'])
            if color != "blue":
                for i in blue[node]:
                    if (i,'blue') not in visited:
                        visited.add((i,'blue'))
                        queue.append([i,length + 1,'blue'])
        return output
            

         


         
        