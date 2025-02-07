# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        for row in board:
            num = set()
            for ele in row :
                if ele != '.' and ele in num:
                    return False
                num.add(ele)
        for i in range(9):
                num = set()
                for j in range(9):
                    if board[j][i] != '.' and board[j][i] in num:
                        return False
                    num.add(board[j][i])
        for row in range(0,9,3):
            
            for col in range(0,9,3):
                subg = set()

                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != '.' and board[row+i][col+j] in subg:
                            return False
                        subg.add(board[row+i][col+j])
        return True






             


                    

                    
            