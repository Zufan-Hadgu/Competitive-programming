# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = nums[0]
      
        while left <= right:
            mid = (left + right) // 2
           
            if mid > 0 and nums[mid] < nums[mid - 1]:  
                ans = nums[mid]
                break  
            
            if nums[mid] >= nums[left] and nums[mid] > nums[right]:
                left = mid + 1  
            else:
                ans = nums[mid]  
                right = mid - 1  
        
        return ans  
