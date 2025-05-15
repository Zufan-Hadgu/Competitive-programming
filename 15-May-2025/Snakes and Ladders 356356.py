# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)

        def gettingRowCol(square):
            r = (square-1)//n
            c = (square-1) % n
            if r % 2 != 0:
                c = n - 1-c
            return (r,c)
        
        queue = deque([(1,0)])
        visited = set()
       
        while queue:
            pos,rols = queue.popleft()
            for i in range(1,7):
                nextSquare = pos  + i
                r,c = gettingRowCol(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == n * n:
                    return rols + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    queue.append([nextSquare,rols + 1])
        return - 1

            
            
            


        