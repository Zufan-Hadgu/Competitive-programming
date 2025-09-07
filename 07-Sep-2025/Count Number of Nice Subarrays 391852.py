# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                prefix[i] =0
            else:
                prefix[i] =1
        prefix_sum = [0]*len(prefix)
        prefix_sum[0] = prefix[0]
        for i in range(1,len(prefix)):
            prefix_sum[i] = prefix[i] + prefix_sum[i-1]
        count = 0
        freq = defaultdict(int)
        freq[0] = 1  # important base case: prefix_sum[i] == k

        for ps in prefix_sum:
            count += freq[ps - k]
            freq[ps] += 1

        return count