# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        isBlock = False
        output = []
        temp = ""

        for line in source:
            j = 0
            while j < len(line):
                if j + 1 < len(line) and line[j] == '/' and line[j + 1] == '/' and not isBlock:
                    break
                elif j + 1 < len(line) and line[j] == '/' and line[j + 1] == '*' and not isBlock:
                    isBlock = True
                    j += 1
                elif j + 1 < len(line) and line[j] == '*' and line[j + 1] == '/' and isBlock:
                    isBlock = False
                    j += 1
                elif not isBlock:
                    temp += line[j]
                
                j += 1

            if temp and not isBlock:
                output.append(temp)
                temp = ""

        return output
