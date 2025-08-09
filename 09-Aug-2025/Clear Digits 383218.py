# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
        