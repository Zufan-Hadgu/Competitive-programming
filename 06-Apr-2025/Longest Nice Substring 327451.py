# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def divide(s):
            d = Counter(s)
            if len(s) <= 1:
                return ""
            for i,char in enumerate(s):
                opposite_case = char.swapcase()
                if opposite_case not in d:
                    left = divide(s[:i])
                    right = divide(s[i+1:])
                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            return s
        return divide(s)





            


             
 
        