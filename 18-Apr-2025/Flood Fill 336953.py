# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction  = [(-1,0),(1,0),(0,-1),(0,1)] 
        original_color = image[sr][sc]
        
        def valid(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])
        
        def dfs(row, col):
            if not valid(row, col) or image[row][col] != original_color or image[row][col] == color:
                return
            image[row][col] = color
            for x, y in direction:
                dfs(row + x, col + y)
        
        if original_color != color:
            dfs(sr, sc)
        
        return image
