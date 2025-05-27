# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        num = 0
        for i in range(len(arr) -1,-1,-1):
            num = max(num,arr[i])
            ans[i-1] = num
        ans[len(arr)-1] = -1
        return ans


     

        