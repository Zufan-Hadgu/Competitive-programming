# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        prc = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                prc[nums[i]*nums[j]] += 1
                
        # print(prc)

        for val in prc.values():
            if val > 1:
                result += (val * (val - 1) // 2) * 8 
        return result
   
        