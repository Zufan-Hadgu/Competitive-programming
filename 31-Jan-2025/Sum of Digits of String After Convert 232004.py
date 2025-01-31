# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str  = ""
        for char in s:
           number =  ord(char) - ord('a') + 1
           num_str += str(number)
           
        to_be_added = int(num_str)
        for i in range(k):
           
            summation = sum([int(d) for d in str(to_be_added)])
            to_be_added = summation
        return to_be_added


        