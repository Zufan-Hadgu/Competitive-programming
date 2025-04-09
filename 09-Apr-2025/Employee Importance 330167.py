# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importance = defaultdict(int)
        

        for employe in employees:
            graph[employe.id].extend(employe.subordinates)
            importance[employe.id] = employe.importance
        def dfs(node,total,visited):
             
            if node in visited:
                return 0
            visited.add(node)

            total = importance[node]
            for negh in graph[node]:
                if negh not in visited:
                    total += dfs(negh,total,visited)
            return total
        return dfs(id,0,set())
                
        