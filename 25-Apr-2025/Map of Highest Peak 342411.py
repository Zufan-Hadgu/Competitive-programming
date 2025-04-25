# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row, col = len(isWater), len(isWater[0])
        queue = deque()
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def valid(i, j):
            return 0 <= i < row and 0 <= j < col

        output = [[float('inf')] * col for _ in range(row)]   
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    output[i][j] = 0
                    queue.append((i, j))

        
        while queue:
            r, c = queue.popleft()
            for x, y in direction:
                new_x, new_y = r + x, c + y
                if valid(new_x, new_y) and output[new_x][new_y] > output[r][c] + 1:
                    output[new_x][new_y] = output[r][c] + 1
                    queue.append((new_x, new_y))

        return output