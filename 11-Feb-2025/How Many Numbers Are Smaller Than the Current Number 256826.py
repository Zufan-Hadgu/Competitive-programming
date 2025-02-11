# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         
        output = []
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if num > nums[i]:
                    count += 1
            output.append(count)
        return output
     