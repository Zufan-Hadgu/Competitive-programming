# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        ans = 0
        def valid(mid):
             
            h_index = 0
            for cite in citations:
                if cite >= mid:
                    h_index += 1
                
            return h_index >= mid
            
        while left <= right:
            mid  = (left + right)//2
            if valid(mid):
                ans = mid
                left = mid + 1
            else:
                 
                right = mid - 1
          
         
        return ans
        