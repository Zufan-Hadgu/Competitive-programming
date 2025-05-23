# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        
    
        up = {x: {2, 3, 4} for x in [2, 5, 6]}
        down = {x: {2, 5, 6} for x in [2, 3, 4]}
        left = {x: {1, 4, 6} for x in [1, 3, 5]}
        right = {x: {1, 3, 5} for x in [1, 4, 6]}
        
        m, n = len(grid), len(grid[0])
        grid[0][0] = -grid[0][0]  # mark as visited
        queue = deque([(0, 0)])

        while queue:
            i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return True
            for k, l, d in [(i-1, j, up), (i+1, j, down), (i, j-1, left), (i, j+1, right)]:
                if 0 <= k < m and 0 <= l < n and -grid[i][j] in d and grid[k][l] in d[-grid[i][j]]:
                    grid[k][l] = -grid[k][l]  # mark as visited
                    queue.append((k, l))
        return False
