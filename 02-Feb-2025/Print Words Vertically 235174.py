# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        len_max = max(len( word) for word  in s)
        result = []
        for i in range(len_max):
            string_n = ""

            for word in s:
                if i < len(word):
                    string_n += word[i]
                else:
                    string_n += " "
            result.append(string_n.rstrip())
        return result



       
        
        
        # for string in s:
        #    for i in range(len(string)):
        #     string_n += string[i]
        #     break
        # result.append(string_n)
        # return result
        


            


        