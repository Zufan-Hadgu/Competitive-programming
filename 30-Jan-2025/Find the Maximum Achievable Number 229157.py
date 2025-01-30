# Problem: Find the Maximum Achievable Number - https://leetcode.com/problems/find-the-maximum-achievable-number/description/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(t):
            num = num + 1
        x = num + t
        return x

        
        