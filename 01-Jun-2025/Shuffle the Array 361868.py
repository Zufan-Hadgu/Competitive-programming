# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        output = []
        while r < len(nums):
            output.append(nums[l])
            output.append(nums[r])
            l += 1
            r += 1
        return output

        