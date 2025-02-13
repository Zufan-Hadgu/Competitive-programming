# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)

        for s in s1:
            d1[s] += 1
        
        r = len(s1)
        l = 0
        while r <= len(s2):
            if d1 == Counter(s2[l:r]):
                return True
            else:
                l += 1
                r += 1
        return False

        

                



        

        
        