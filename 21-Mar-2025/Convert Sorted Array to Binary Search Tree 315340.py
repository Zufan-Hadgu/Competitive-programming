# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        m = len(nums)//2 
        val = nums[m]
     
        left = nums[:m]
        right = nums[m+1:]
        first = TreeNode(val)
        first.left = self.sortedArrayToBST(left)
        first.right = self.sortedArrayToBST(right)
        return first
    


        
 

        