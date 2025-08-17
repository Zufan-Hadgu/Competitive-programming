# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = sum(1 for count in freq.values() if count == maxFreq)
        
        partCount = maxFreq - 1
        partLength = n + 1
        emptySlots = partCount * partLength + maxCount
        
        return max(len(tasks), emptySlots)