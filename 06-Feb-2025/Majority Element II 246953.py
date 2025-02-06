# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        a = n//3
        appear = defaultdict(int)
        result = []
        for num in nums:
            appear[num] += 1
        for key,value in appear.items():
            if value > a:
                result.append(key)
                
        return result

        