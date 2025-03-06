# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
            if token == "+":
                if len(stack)>=2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = val1 + val2
                    stack.append(new_val)
            elif token == "-":
                if len(stack)>=2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = val2 - val1
                    stack.append(new_val)
            elif token == "*":
                if len(stack)>=2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = val1 * val2
                    stack.append(new_val)
            elif token == "/":
                if len(stack)>=2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    new_val = int(val2 / val1)
                    stack.append(new_val)
        return stack[0]
                

        