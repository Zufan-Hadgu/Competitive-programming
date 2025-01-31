# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if command[i] =="G":
                result+= "G"
            if command[i] =="(":
                if command[i+1].isalpha():
                    result+= "al"
                else:
                    result+= "o"
        return result
    