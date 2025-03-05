# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def sortpoints(point):
            return point[1]
        points.sort(key =sortpoints)

        print(points)

        arrow = 0
        common = float('-inf')
        for start,end in points:
            if start > common:
                arrow += 1
                common = end
        return arrow 
 

        