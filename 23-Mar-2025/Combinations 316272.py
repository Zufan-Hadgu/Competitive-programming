# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(firstnum,path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for candidate in range(firstnum,n+1):
                path.append(candidate)
                backtrack(candidate+1,path)
                path.pop()
        backtrack(1,[])
   
        return ans
        # ans = []
        # def backtrack(firstnum,path):
        #     if len(path) == k:
        #         ans.append(path)
        #         return 
        #     if firstnum > n:
        #         return 
        #     path.append(firstnum)
        #     backtrack(first)




        