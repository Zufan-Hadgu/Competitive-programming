# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      
        output = []
        top = 0
        left = 0 
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            
            for col in range(left,right + 1):
                output.append(matrix[top][col])
                
            top += 1
            for row in range(top,bottom + 1):
                output.append(matrix[row][right])
            
            right -= 1
            if left > right or top > bottom:
                break
             
            for col in range(right,left - 1,-1):
                output.append(matrix[bottom][col])
            bottom -= 1
    

            for row in range(bottom, top - 1, -1):
                output.append(matrix[row][left])
            left += 1


        return output
        





 
        