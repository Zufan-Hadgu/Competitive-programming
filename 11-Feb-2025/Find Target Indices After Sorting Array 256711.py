# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution(object):
     
    def targetIndices(self, nums, target):
          
        nums = sorted(nums)
         
        new_list = []
        for i in range(len(nums)):

            if nums[i] ==target:
                new_list.append(i)
        return new_list
                


        