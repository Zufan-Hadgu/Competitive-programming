# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(i):
            if i >= len(questions):
                return 0
            state = i
            if state not in memo:
                memo[state] = max(questions[i][0] + dp(i+1+questions[i][1]),dp(i+1))
            return memo[state]
        return dp(0)