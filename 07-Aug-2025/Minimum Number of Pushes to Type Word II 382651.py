# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        output = 0
        values = []

        for key, value in d.items():
            values.append(value)
    
        pushes = sorted(values, reverse=True)
        count = 0
        for i in range(len(pushes)):
            if count < 8:
                output += pushes[i]
            elif count < 16:
                output += 2 * pushes[i]
            elif count < 24:
                output += 3 * pushes[i]
            else:
                output += (count // 8 + 1) * pushes[i]
            count += 1

        return output