# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        window = sum(nums[:k])
        d = Counter(nums[:k])
        N = len(d)
        output = 0

        if N == k:
            output = window

        l = 0
        r = k

        while r < len(nums):
            out_elem = nums[l]
            d[out_elem] -= 1
            if d[out_elem] == 0:
                del d[out_elem]

            in_elem = nums[r]
            d[in_elem] = d.get(in_elem, 0) + 1

            window += in_elem - out_elem
            N = len(d)

            if N == k:
                output = max(output, window)

            l += 1
            r += 1

        return output
