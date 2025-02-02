# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        number = 0
        for i in range(n):
            number += digits[i] * 10**(n-i-1)
        number += 1
        number_list = []
        for digit in str(number):
            number_list.append(int(digit))
        return number_list




        