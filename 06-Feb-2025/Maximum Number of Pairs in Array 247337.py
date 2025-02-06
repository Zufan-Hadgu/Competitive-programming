# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        print(d)
        
        paird = 0
        unpaird = 0

        for key,value in d.items():
            if value % 2 == 0:
                paird += value//2
            else:
                paird += value//2
                unpaird += value % 2
        return [paird,unpaird]



      
