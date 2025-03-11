# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factor(n):
            if n == 0 or n == 1:
                return 1
            
            return n*factor(n-1)

        def trailingZero(number):
            if number % 10 != 0:
                return 0
            return 1 + trailingZero(number//10)
        
        factorial = factor(n)
        ans = trailingZero(factorial)
        return ans


        



        