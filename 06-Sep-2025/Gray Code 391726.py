# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            # Reflect and prefix 1 to the reflected half
            result += [x | (1 << i) for x in reversed(result)]
        return result

        