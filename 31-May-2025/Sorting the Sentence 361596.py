# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        output = [0]*len(words)
        for word in words:
            position = int(word[-1])
            output[position-1] = word[:-1]
        return " ".join(output)
         
        

        