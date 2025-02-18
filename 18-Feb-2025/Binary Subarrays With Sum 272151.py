# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        n = len(nums)
        output = 0
        for i in range(1,n):
            nums[i] += nums[i-1]

        for currsum in nums:
            output += d[currsum-goal] 
            d[currsum] += 1
        return output
        

        