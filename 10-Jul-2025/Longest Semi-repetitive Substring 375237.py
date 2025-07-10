# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        i = 0
        j = 1   
        if len(s) == 1:
            return 1
        max_length = 0
        repetitive = 0
        while j < len(s):
            if s[j] == s[j-1]:
                repetitive += 1
            while repetitive > 1:
                if i + 1 < len(s) and s[i + 1] == s[i]:
                    repetitive -= 1
                i += 1
            max_length =max(max_length, j - i  + 1)
            j += 1
        return max_length

            


        