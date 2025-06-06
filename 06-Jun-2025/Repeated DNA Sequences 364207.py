# Problem: Repeated DNA Sequences - https://leetcode.com/problems/repeated-dna-sequences/

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
 
        left = 0
        dict_of_word = {}
        for i in range(len(s) - 9):
            new_word = s[i:i+10]
            if new_word in dict_of_word:
                dict_of_word[new_word] += 1
            else:
                dict_of_word[new_word] = 1
        return [word for word, count in dict_of_word.items() if count > 1]








        