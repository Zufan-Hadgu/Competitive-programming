# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = 0
        closestsum  = float('inf')
        nums.sort()

        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) -1 
            while l < r:
                currentsum = nums[i] + nums[l] + nums[r]
                if abs(currentsum - target) < abs(closestsum - target):
                    closestsum = currentsum
                if currentsum < target:
                    l += 1
                elif currentsum > target:
                    r -= 1
                else:
                    return currentsum
        return closestsum 