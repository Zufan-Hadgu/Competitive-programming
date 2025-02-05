# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n = len(list1)
        m = len(list2)
        least_index = float('inf')
        result = []
        for i in range(n):
            for j in range(m):
                if list1[i] == list2[j]:
                    least = i + j
                    if least < least_index:
                        result = [list1[i]]
                        least_index = min(least,least_index)  
                    elif least == least_index:
                        result.append(list1[i])      
        return(result)
     
     
            
                 


        