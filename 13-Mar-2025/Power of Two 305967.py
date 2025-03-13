# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        result = math.log2(n)
        return result.is_integer()
        