# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # acc = 1
        n = len(nums)
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        print(prefix)
        output = [1]*n


        
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
    
         
        for i in range(n -2 ,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
    

        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        return output
        

        



        # print(prefix)

         

         



        