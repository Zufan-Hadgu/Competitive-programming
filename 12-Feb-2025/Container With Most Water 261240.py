# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        water = float('-inf')
        while l < r:
            y = min(height[l], height[r])
            x = r - l 
            area = y * x
            water = max(water,area)
            if height[l] <= height[r]:
                 l += 1
            else:
                r -= 1
        return water




        