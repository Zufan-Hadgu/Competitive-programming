# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        strs = Counter(s)
        if letter in strs.keys():
            result = floor((strs[letter] /len(s)) *100)
            return result
            
        else:
            return 0
        


        