# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
          
        left = 1
        right = max(candies)
        ans = 0
        def valid(target):
            child = 0
            for candy in candies:
                if candy >= target:
                    add = candy//target
                    child += add
                 
                 
            return child >= k

        while left <= right:
            mid = (left + right)//2
            if valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
           
          
        return ans

        