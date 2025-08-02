# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                 stack.append(s[i])
            elif s[i] == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])    
        return len(stack)

           

        