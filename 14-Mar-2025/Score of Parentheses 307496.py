# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                number = 0
                while stack and stack[-1] != '(':
                    number += stack.pop()
                stack.pop()
                if number == 0:
                    stack.append(1)
                else:
                    stack.append(2*number)
        return stack[0] if len(stack) == 1 else sum(stack)