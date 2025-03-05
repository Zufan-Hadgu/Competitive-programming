# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        signs = path.split("/")
        print(signs)

        stack = []
        for sign in signs:
            if sign == "..":
                if stack:
                    stack.pop()
            elif sign == "." or sign == "":
                continue
            else:
                stack.append(sign)
        return "/" + "/".join(stack)

        