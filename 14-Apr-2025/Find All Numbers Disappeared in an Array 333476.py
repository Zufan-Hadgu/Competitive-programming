# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
         
        for i , n in enumerate(nums):
            if n > 0:
                answer.append(i + 1)
        return answer
        


        