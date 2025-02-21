# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums))
         

        for start,end in requests:
            prefix[start] += 1
            if end+1 < len(nums):
                prefix[end+1] += -1
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
      
        prefix.sort()
        nums.sort()

        answer=sum(num*freq for num,freq in zip(nums,prefix))

        return answer%(10**9 + 7)

        # print(prefix)


        
            
        