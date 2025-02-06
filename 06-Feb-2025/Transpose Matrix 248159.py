# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newM = []
        for i in range(len(matrix[0])):
            newM.append([0]*len(matrix))
        print(newM)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newM[j][i] = matrix[i][j]
        return newM
    


#using zip() build in function 
        # transpose = list(zip(*matrix))
        # return transpose


        