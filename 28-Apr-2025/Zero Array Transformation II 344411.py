# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        need = nums[:]
        k = 0
        
        for li, ri, vali in queries:
            for i in range(li, ri + 1):
                dec = min(need[i], vali)
                need[i] -= dec
            k += 1
            if all(x == 0 for x in need):
                return k
        
        return -1
