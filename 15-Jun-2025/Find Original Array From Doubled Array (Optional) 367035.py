# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return [] 
        changed.sort()
        freq = {}
        for num in changed:
            freq[num] = freq.get(num, 0) + 1
        output = []
        
        for num in changed:
            if freq[num] == 0:
                continue  
            double = num * 2
            if freq.get(double, 0) == 0:
                return []  
            output.append(num)
            freq[num] -= 1
            freq[double] -= 1
        
        return output
