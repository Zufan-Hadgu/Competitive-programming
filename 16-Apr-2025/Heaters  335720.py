# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        i = 0   
        res = 0
        
        for house in houses:
            
            while i + 1 < len(heaters) and abs(heaters[i+1] - house) <= abs(heaters[i] - house):
                i += 1
            res = max(res, abs(heaters[i] - house))
        
        return res
