# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n:
            output += n & 1
            n = n >> 1
        return output 
        # def binary(n):
        #     if n == 0:
        #         return "0"
        #     Bit = ""
        #     while n > 0:
        #         rem = n % 2
        #         Bit = str(rem) + Bit
        #         n = n // 2
        #     number = Counter(Bit)
        #     return number["1"]
        # return binary(n)
        