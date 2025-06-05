# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        output = []
        for x,y in points:
            d = sqrt(x**2 + y**2)
            distance.append((d,[x,y]))
        distance.sort()
        for _ in range(k):
           output.append(distance[_][1])
        return output

        