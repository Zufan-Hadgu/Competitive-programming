# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            num = (columnNumber - 1) % 26
            char = chr(65 + num)
            result.append(char)
            columnNumber = (columnNumber - 1) // 26
            new_result = "".join(result)
        return (new_result[::-1])

            
       
       
       
       
       
        # excel = []
        # while columnNumber > 26:
        #     Num = columnNumber // 26
        #     if Num < 26:
        #         excel.append(chr(64 + Num))
        #     else:
        #         Num = Num//26

        # string_n = ""
        # if columnNumber <= 26:
        #     letter_num = ord('A') + columnNumber - 1
        #     string_n += chr(letter_num)
        # elif columnNumber > 26:
        #     first_letter = columnNumber//26
        #     letter_num = ord('A') + first_letter - 1
        #     remaning = columnNumber % 26
        #     string_n += chr(letter_num)
        #     if remaning > 0:
        #         remaning = ord('A') + remaning - 1
        #         string_n += chr(remaning)
       
                
        # return string_n

