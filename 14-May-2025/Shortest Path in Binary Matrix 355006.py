# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def valid(i,j):
            return 0 <= i < n and 0 <= j < n and  grid[i][j] == 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1 
        q = deque([(0,0,1)])
        visited = set([(0,0)])
        directions = [(1,-1),(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1)]

        while q:
            x,y,length = q.popleft()
            if (x,y) == (n-1,n-1):
                return length
            
            for dy,dx in directions:
                if valid(x + dx, y + dy) and (x + dx , y + dy) not in visited:
                    q.append((x + dx,y+dy,length + 1))
                    visited.add((x+dx,y+dy))
        return -1
                

        