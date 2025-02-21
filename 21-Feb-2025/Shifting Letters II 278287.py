# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for start,end,drn in shifts:
            if drn == 1:
                value = 1
            else:
                value = -1
            prefix[start] += value
            prefix[end+1] -= value
            
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1] 
   
        
        for i in range(len(prefix)):
            prefix[i] = prefix[i] % 26
      

        new_word = []

        for i in range(len(s)):
            new_unicode  = ord(s[i]) + prefix[i]
            if new_unicode > 122:
                new_unicode -= 26
            if new_unicode < 97:
                new_unicode += 26
            new_word.append(chr(new_unicode))
        return ''.join(new_word)
        

 

            

        