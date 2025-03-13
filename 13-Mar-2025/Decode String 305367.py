# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = []
        digit = 0
          
        for char in s:
            if char.isdigit():
                digit = digit*10 + int(char)
            elif char == '[':
                number.append(digit)
                stack.append(char)
                digit = 0
            elif char == "]":
                charac = ''
                while stack[-1] != "[":
                    charac  = stack.pop() + charac
                stack.pop()
                updated = number.pop() *charac
                stack.append(updated)    
            else:
                stack.append(char)
        return ''.join(stack)
                


       