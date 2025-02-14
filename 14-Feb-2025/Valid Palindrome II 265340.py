# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break

        return s[:l] + s[l+1:] ==(s[:l] + s[l+1:])[::-1] or s[:r] + s[r+1:] ==(s[:r] + s[r+1:])[::-1]
                 
        