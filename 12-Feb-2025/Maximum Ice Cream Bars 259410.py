# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        s = sorted(costs)
        total = 0
        count = 0
        for i in range(len(s)):
            total += s[i]        
            if total <= coins:
                count += 1     
        return count
            
       

        