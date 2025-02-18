# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        for i in range(1,n):
            nums[i] += nums[i-1]

        for num in nums:
            count += d[num%k]
            d[num%k] += 1
        return count
        

     




        