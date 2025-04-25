# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        output = [[float('inf')] *len(mat[0]) for _ in range(len(mat))]
        queue = deque()
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def valid(i, j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    queue.append((i,j))
        while queue:
            row,col = queue.popleft()
            for x,y in direction:
                new_x = row + x
                new_y = col + y
                if valid(new_x,new_y) and output[new_x][new_y] > output[row][col] + 1:
                
                        output[new_x][new_y] = output[row][col] + 1
                        queue.append((new_x,new_y))
        return output



                

        

        


        
        