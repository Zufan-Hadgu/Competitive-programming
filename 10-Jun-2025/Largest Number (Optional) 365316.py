# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = ''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if int(str(nums[i]) + str(nums[j])) > int(str(nums[j]) + str(nums[i])):
                    nums[i],nums[j] = nums[j] , nums[i]
         
        for num in nums:
            s +=str(num)
        
        if s[0] == '0':
            return '0'
        return s
    

    
        





        
                

     
         


        