# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        incomming = [0 for i in range(numCourses)]
        output = []
        queue = deque()

        for course,preque  in prerequisites:
            graph[preque].append(course)
            incomming[course] += 1
         

        for course in range(numCourses):
            if incomming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            output.append(course)

            for g in graph[course]:
                incomming[g]  -= 1
                if incomming[g] == 0:
                    queue.append(g)
        if len(output) != numCourses:
            return []
        return output



        