# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_num = {
           "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        n = len(s)
        result = 0
        i = 0

        while i < n:

            if i < n - 1 and s[i] == 'C' and s[i+1] == 'M':
                result += dict_num['M'] - dict_num['C']
                i += 2
            elif i < n - 1 and s[i] == 'C' and s[i+1] == 'D':
                result += dict_num['D'] - dict_num['C']
                i += 2
            elif i < n - 1 and s[i] == 'X' and s[i+1] == 'L':
                result += dict_num['L'] - dict_num['X']
                i += 2
            elif  i < n - 1 and s[i] == 'X' and s[i+1] == 'C':
                result += dict_num['C'] - dict_num['X']
                i += 2
            elif i < n - 1 and s[i] == 'I' and s[i+1] == 'V':
                result += dict_num['V'] - dict_num['I']
                i += 2
            elif i < n - 1 and s[i] == 'I' and s[i+1] == 'X':
                result += dict_num['X'] - dict_num['I']
                i += 2
                 
            else:
                result += dict_num[s[i]]
                i += 1
        return result

         
       