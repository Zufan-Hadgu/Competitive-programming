# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s.lower():
            if char.isalnum():
                result += char
     
        print(result)
        reversed_word = result[::-1]
        return reversed_word == result

    
    

        