# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time, fresh = 0, 0
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def valid(i, j):
            return 0 <= i < row and 0 <= j < col and grid[i][j] == 1
        
        while queue and fresh > 0:
            for _ in range(len(queue)):  # Iterate over current level size
                r, c = queue.popleft()

                for x, y in direction:
                    new_x = x + r
                    new_y = y + c

                    if not valid(new_x, new_y):
                        continue

                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1