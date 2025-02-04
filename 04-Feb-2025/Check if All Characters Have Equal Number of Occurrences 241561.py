# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = defaultdict(int)
        values = []
        for char in s:
            d[char] += 1

        for key, val in d.items():
            values.append(val)
       
        counted = Counter(values)
        return len(counted) == 1



      