# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotet(mat: List[List[int]]):
            Rotated = []
            for i in range(len(mat)):
                row = []
                for j in range(len(mat[0])):
                    row.append(mat[j][i])
                Rotated.append(row)

            for i in range(len(Rotated)):
                Rotated[i] = Rotated[i][::-1]

            return Rotated
        i = 0
        while i < 4:
            if mat == target:
                return True
            else:
                mat = rotet(mat)
                i += 1
        return False