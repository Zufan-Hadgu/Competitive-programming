# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])
        print(d)
        for key,lists in d.items():
            if key % 2 ==0:
                for num in lists[::-1]:
                     result.append(num)
            else:
                for num in lists:
                    result.append(num)

        return result



    
                 
    

        