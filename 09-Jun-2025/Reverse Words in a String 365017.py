# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        parts = s.split(' ')
        print(parts)
        output = []

        for i in range(len(parts)-1, -1 , -1 ):
            if parts[i] != '':
                output.append(parts[i])
    
        return (" ".join(output))



    


        