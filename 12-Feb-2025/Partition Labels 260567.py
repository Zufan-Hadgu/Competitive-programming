# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        output = []
    
        for i in range(len(s)):
            d[s[i]] = i
        l = 0
        r = 0 
        for j in range(len(s)):
            r = max(r, d[s[j]])
            if j == r:
                output.append(r + 1-l)
                l = r + 1
        return output 
            
       

       
       






 


       
        