# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

from collections import defaultdict

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  
        count_stack = [] 

        for char in s:
            if stack and stack[-1] == char:
                count_stack[-1] += 1
                stack.append(char)
                if count_stack[-1] == k:
                    for _ in range(k):
                        stack.pop()
                    count_stack.pop()
            else:
                stack.append(char)
                count_stack.append(1)

        return ''.join(stack)