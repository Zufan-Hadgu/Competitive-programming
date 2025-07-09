# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        grid2 = [[0] * (n * 3) for _ in range(n * 3)]

        for i in range(n):
            for j in range(n):
                r, c = i * 3, j * 3
                if grid[i][j] == '/':
                    grid2[r][c + 2] = 1
                    grid2[r + 1][c + 1] = 1
                    grid2[r + 2][c] = 1
                elif grid[i][j] == '\\':
                    grid2[r][c] = 1
                    grid2[r + 1][c + 1] = 1
                    grid2[r + 2][c + 2] = 1

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n * 3 or c >= n * 3 or grid2[r][c] != 0:
                return
            grid2[r][c] = 2   
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r + dr, c + dc)

        count = 0
        for r in range(n * 3):
            for c in range(n * 3):
                if grid2[r][c] == 0:
                    dfs(r, c)
                    count += 1

        return count