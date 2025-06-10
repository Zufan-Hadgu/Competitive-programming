# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        b = sorted(heights)
        output = 0
        i = 0
        while i < len(b):
            if heights[i] != b[i]:
                output += 1
            i += 1
        return output

        