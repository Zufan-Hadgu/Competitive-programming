# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)   
        right = sum(weights)   
        ans = right

        def valid(target):
            total_weight = 0
            required_days = 1

            for weight in weights:
                if total_weight + weight > target:
                    required_days += 1
                    total_weight = weight
                else:
                    total_weight += weight

            return required_days <= days

        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
