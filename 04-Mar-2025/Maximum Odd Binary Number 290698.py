# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = -1
        new_s = ["0"] * len(s)
        new_s[-1] = "1"
        for l in s:
            if l == '1':
                count_one += 1
        for i in range(count_one):
            new_s[i] = "1"
            
        return (''.join(new_s))


        