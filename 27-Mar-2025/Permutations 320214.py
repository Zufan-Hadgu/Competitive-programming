# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        ans = []
        def perm(path ):
            nonlocal ans
            if len(path) == len(nums):
                ans.append(path[:])
                return

          

            for num in nums:
                if num not in path:
                    path.append(num)
                    perm(path)
                    path.pop()
        perm([])
        return ans

        