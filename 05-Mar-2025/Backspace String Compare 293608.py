# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for letter in s:
            if letter == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(letter)

        for letter in t:
            if letter == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(letter)
        if ''.join(stack1) == ''.join(stack2):
            return True
        else:
            return False
        