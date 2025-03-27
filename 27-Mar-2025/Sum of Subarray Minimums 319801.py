# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []
        total = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                val = stack.pop()
                left = stack[-1]
                right = i
                total += arr[val] *(val-left)*(right-val)       

            stack.append(i)
        return total%(10**9 + 7)



         
        




 
       