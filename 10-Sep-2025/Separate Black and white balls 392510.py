# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0 
        swap = 0

        for i in range(len(s)):
            if s[i] == '0':
                swap += black
                # print(swap)
            else:
                black += 1
        return swap


        
        