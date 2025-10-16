# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count_sub_arr = 0
        for i in range(len(nums)):
            val = 0
            for j in range(i,len(nums)):
                val = math.gcd(val,nums[j])  
                if val == k:
                    count_sub_arr += 1
        return count_sub_arr

        