# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        result = []
        
        for current in intervals:
            start, end = current
            
            if not result:
                result.append([start, end])
            else:
                last_start, last_end = result[-1]
                
                if start <= last_end: 
                    result[-1][1] = max(last_end, end)
                else:
                    result.append([start, end])
        
        return result