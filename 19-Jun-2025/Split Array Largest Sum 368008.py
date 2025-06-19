# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
       
        def can_split(max_sum):
            count = 1
            current = 0
            for num in nums:
                if current + num > max_sum:
                    count += 1
                    current = num
                else:
                    current += num
            return count <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left