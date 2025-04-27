# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

from collections import deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        prereq = [[False] * numCourses for _ in range(numCourses)]
        incomming = [0] * numCourses
        queue = deque()

        for pre, course in prerequisites:
            graph[pre].append(course)
            incomming[course] += 1
            prereq[pre][course] = True
        
        for course in range(numCourses):
            if incomming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                for i in range(numCourses):
                    if prereq[i][course]:
                        prereq[i][next_course] = True
                prereq[course][next_course] = True
                incomming[next_course] -= 1
                if incomming[next_course] == 0:
                    queue.append(next_course)
        
        result = []
        for u, v in queries:
            result.append(prereq[u][v])
        
        return result
