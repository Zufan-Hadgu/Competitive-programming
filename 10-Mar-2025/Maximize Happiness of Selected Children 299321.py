# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        happy = 0
        for i in range(1,k+1):
            happy += happiness[-1]
            happiness.pop()
            if happiness:   
                happiness[-1] = happiness[-1] - i 
                if happiness[-1] < 0:
                    happiness[-1] = 0   
        return happy
