# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
        revelded = set()
        output = [[0]*len(board[0]) for _ in range(len(board))]

        def valid(i,j):
           return  0 <= i < len(board) and 0 <= j < len(board[0]) 
 
        def count_adjecent(i,j):
            count = 0

            for x,y in direction:
                new_x = i + x
                new_y = j + y
                if valid(new_x,new_y) and board[new_x][new_y] == "M":
                    count += 1

            return count
      
        def dfs(i,j):
            if not valid(i,j) or board[i][j] != "E":
   
                return 
            mines = count_adjecent(i,j)
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = "B"
                for x, y in direction:
                    dfs(i + x, j + y)



        i,j = click[0],click[1]

       
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        else:
            dfs(i,j)
            
        return board







                    
        