# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibo(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]
        return fibo(n)
         