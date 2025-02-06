# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        answer = []

        for key,value in counted.items():
            if value == 2:
                answer.append(key)
        return answer





 #with o(n2) time and o(1) space 
        # answer = []
    
        # while len(nums) != 0:
        #     a = nums[0]
        #     nums.remove(a)
        #     if a in nums:
        #         answer.append(a)
        # return answer
        