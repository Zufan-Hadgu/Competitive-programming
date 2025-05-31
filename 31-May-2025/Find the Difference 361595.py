# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        new_list = list(s)
        for letter in t:
            if letter in new_list:
                new_list.remove(letter)
            else:
                return letter 
        
        