# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        end = len(graph) - 1
        start = 0

        queue = deque([(start,[start])])
        output = []

        while queue:

            node,path = queue.popleft()
            if node == end:
                output.append(path)
 
            for neighbr in graph[node]:
               queue.append((neighbr,path + [neighbr]))
                
        return output
            
            




    
        