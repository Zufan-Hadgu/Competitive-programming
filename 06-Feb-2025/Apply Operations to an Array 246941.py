# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0 
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            i += 1
        num2 = []
        count = 0
        for num in nums:
            if num != 0:
                num2.append(num)
            else:
                count += 1
            
        return num2 + [0]*count

         
       
            

            