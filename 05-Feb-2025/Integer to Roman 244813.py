# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        Romans = {
           1:"I",
           5: "V",	
           10: "X",	
           50: "L",	
            100: "C",	
            500: "D",	
            1000: "M"

        }
        
        
        result = ""
        n = len(str(num))
        while num > 0:     
            val = num//(10**(n-1))
            num %= 10**(n-1)

            if val * 10**(n-1) in Romans:
                result += Romans[val * 10**(n-1)]
            else:
                if val < 5 and val != 4:
                    result += val * Romans[10**(n-1)]
                elif val > 5 and val != 9:
                    result += Romans[5*10**(n-1)] + (val - 5)* Romans[10**(n-1)]
                elif val == 4:
                    result += Romans[10**(n-1)] + Romans[5* 10**(n-1)]
                elif val == 9:
                    
                    result += Romans[10**(n-1)] + Romans[10**(n)]
            n-= 1
        return result
                
                    

             



 