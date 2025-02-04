# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        print(counted)
        result = []
        for key, val in counted.items():
            if val > 1:
                result.append(key)
        return result
