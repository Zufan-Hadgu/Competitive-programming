# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        temp = x 
        while x > 0:
            rem = x % 10
            result = result * 10 + rem
            x = x//10
        return result == temp
        


        