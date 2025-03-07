# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

 class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decr = deque()
        incr = deque()
        output = 0
        l = 0
        ans = 0

        for r in range(len(nums)):
            while decr and decr[-1] < nums[r]:
                decr.pop()
            decr.append(nums[r])
    
            while incr and incr[-1] > nums[r]:
                incr.pop()
            incr.append(nums[r])
        
         
            while decr[0] - incr[0] > limit:
                val = nums[l]
                if decr[0] == val:
                    decr.popleft()
                if incr[0] == val:
                    incr.popleft()
                l += 1
            ans = max(ans,r-l+1)
        return ans
