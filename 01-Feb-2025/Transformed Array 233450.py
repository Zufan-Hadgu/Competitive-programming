# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] > 0:
                index =( nums[i] + i)%n
                result[i] = nums[index]
            elif nums[i] < 0:
                index = ((i - abs(nums[i])) + n)%n
                result[i] = nums[index]
            else:
                result[i] = nums[i]
        return result



        