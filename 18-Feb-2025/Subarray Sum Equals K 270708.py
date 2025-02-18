# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum=0
        count=0
        diction=defaultdict(int)
        diction[0]=1
        for num in nums:
            cursum+=num  
            count+=diction[cursum-k]
            diction[cursum]+=1

        return count