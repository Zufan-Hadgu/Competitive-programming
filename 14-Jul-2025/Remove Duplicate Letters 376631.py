# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_position = {char: i for i, char in enumerate(s)}
        output = []
        visited = set()

        for i, char in enumerate(s):
            if char in visited:
                continue
            while output and char < output[-1] and last_position[output[-1]] > i:
                visited.remove(output.pop())
            visited.add(char)
            output.append(char)

        return ''.join(output)