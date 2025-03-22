# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = 0
        def combination(l,path):
            ans.append(path[:])
            for candidate in range(l,len(nums)):
                path.append(nums[candidate])
                combination(candidate+1,path)
                path.pop()
        combination(0,[])
        return ans
            

        