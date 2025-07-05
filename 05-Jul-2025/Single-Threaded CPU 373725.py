# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        indexed_tasks.sort()  

        result = []
        heap = []   
        time = 0
        i = 0   

        while i < n or heap:
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            if heap:
                proc_time, idx = heapq.heappop(heap)
                time += proc_time
                result.append(idx)
            else:
                
                time = indexed_tasks[i][0]

        return result