# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_s = s.split()
        n = len(list_s)
        return len(list_s[n-1])

        