# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph2=[[] for j in range(len(graph))]
        for g in range(len(graph)):
            for num in graph[g]:
                graph2[num].append(g)
      

         
        outcomming = [0 for i in range(len(graph))]
        
        output=[]
        queue = deque()

        for i in range(len(graph)):
            outcomming[i] = len(graph[i])
     

        for g in range(len(graph)):
            if outcomming[g] == 0:
                queue.append(g)

        while queue:
            course = queue.popleft()
            output.append(course)

            for g in graph2[course]:
                outcomming[g]  -= 1
                if outcomming[g] == 0:
                    queue.append(g)


        ans=sorted(output)
        return ans



        
            
        
         




        