# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            n = s.index('@')
            s = s.lower()
            return (s[0] + "*****" +s[n-1:])
        new_s = ''
        for char in s:
            if char.isdigit():
                new_s += char
        
        if len(new_s) == 10:
            return "***-***-" + new_s[-4:]
        elif len(new_s) == 11:
            return "+*-***-***-" + new_s[-4:]
        elif len(new_s) == 12:
            return "+**-***-***-" + new_s[-4:]
        elif len(new_s) == 13:
            return "+***-***-***-" + new_s[-4:]



           

       

 
        