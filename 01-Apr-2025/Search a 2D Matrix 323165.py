# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = 0
        while m < len(matrix):
            if target in matrix[m]:
                return True
            else:
                m = m + 1
        return False
        
        