# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []   
        for num in nums:
            for char in str(num):
                ans.append(int(char))
        return ans
            
            
        