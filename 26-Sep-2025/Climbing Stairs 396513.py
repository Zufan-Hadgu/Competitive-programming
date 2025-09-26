# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # prev1, prev2 = 2, 1
        # for _ in range(3, n + 1):
        #     current = prev1 + prev2
        #     prev2 = prev1
        #     prev1 = current

        # return prev1

        # top(3) = top(2) + top(1) 
        #           1 + 1  + 1
        #           2


        memo = {}
        def Stairs(n):
            if n in memo:
                return memo[n]
            if n < 3:
                return n
            memo[n] = Stairs(n-1) + Stairs(n-2)
            return memo[n]
        return Stairs(n)

            