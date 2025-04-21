# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        print(graph)

        queue = deque([(headID,0)])
        output = 0
        while queue:
            i,time = queue.popleft()
            output = max(output,time)

            for emp in graph[i]:
                queue.append((emp,time + informTime[i]))
        return output

        