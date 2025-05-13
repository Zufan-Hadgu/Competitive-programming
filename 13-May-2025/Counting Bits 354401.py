# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        def binary(n):
            if n == 0:
                return "0"
            Bit = ""
            while n > 0:
                rem = n % 2
                Bit = str(rem) + Bit
                n = n // 2
            return Bit

        for i in range(n+1):
            number = binary(i) 
            dic = Counter(number)
            ans.append(dic["1"] if "1" in dic else 0)
        return ans
