# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        def valid(i,j):
            return 0 <= i <len(grid) and 0 <= j < len(grid[0])
        

        def dfs(row,col):
            if  not valid(row,col) or grid[row][col] == 0:
                return 0
            ans = grid[row][col]
            grid[row][col] = 0
            for x,y in direction:
                new_row = x + row
                new_col = y + col
                ans += dfs(new_row,new_col)
                
            
            return ans
        area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = dfs(i, j)
                    area = max(area,res)
                    
        return area
        