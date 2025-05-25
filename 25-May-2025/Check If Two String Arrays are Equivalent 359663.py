# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new = ""
        for word in word1:
            new += word   
        new2 = ""
        for word in word2:
            new2 += word 
        if new == new2:
            return True
        else:
            return False
        