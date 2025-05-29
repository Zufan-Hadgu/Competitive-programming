# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = j =0
        merged = ""
        while i<len(word1) and j<len(word2):
            merged += word1[i] + word2[j]
            i +=1
            j +=1
        if i<len(word1):
            merged += word1[i:]

        else:
            merged += word2[j:]
        return merged

        
        

        

        return "" .join(character_to_be_merged)
        

        