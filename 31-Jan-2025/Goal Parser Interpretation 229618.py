# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution(object):
 def interpret(self, command):
     
    d = {
        'G': 'G',
        '()': 'o',
        '(al)': 'al'
    }
    
     
    parser = ""
    
     
    i = 0
    while i < len(command):
        if command[i] == 'G':
            parser += d['G']
            i += 1
        elif command[i:i+2] == '()':
            parser += d['()']
            i += 2
        elif command[i:i+4] == '(al)':
            parser += d['(al)']
            i += 4
        else:
             
            i += 1
    
    return parser

