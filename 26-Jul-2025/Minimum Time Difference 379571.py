# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m
        
        minutes = sorted(to_minutes(t) for t in timePoints)
        min_diff = float('inf')

        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

       
        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])

        return min_diff