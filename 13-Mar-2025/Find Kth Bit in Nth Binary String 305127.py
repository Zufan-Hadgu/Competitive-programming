# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            new_s = []
            for number in s:
                if number == '0':
                    new_s.append('1')
                else:
                    new_s.append('0')
            return ''.join(new_s)
        def reverse(s):
            return s[::-1]
        def nthbinary(n):
            if n == 1:
                return "0"
            else:
                Sn = nthbinary(n - 1) + "1" + reverse(invert(nthbinary(n-1)))
            return Sn
        ans = nthbinary(n)
        return ans[k-1]
            
        