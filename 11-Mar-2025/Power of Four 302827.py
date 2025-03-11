# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
            
        def power(n):
            if n == 1:
                return True
            if n % 4 != 0:
                return False
                
            return power(n//4)
        ans = power(n)
        return ans
        