# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        output = 0
        while x or y:
            last = x & 1
            lasty = y & 1
            if last != lasty:
                output += 1
            x  = x >> 1
            y = y >> 1
        return output

           